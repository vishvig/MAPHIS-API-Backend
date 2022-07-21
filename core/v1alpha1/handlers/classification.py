import json

from ..models.endpoints.request.classification import *

from utils import *

from utils.mongo_util import mongo_conn
from utils.redis_utils import RedisUtils
from utils.common_utils import CommonUtils
from utils.logger_util import get_logger

from constants.configurations import Db

LOG = get_logger()


class ClassifyHandler(object):
    def __init__(self):
        self._cu_ = CommonUtils()

        self.conn = mongo_conn
        self.cache = RedisUtils()
        self.db_name = Db.mongo_db_name
        self.shapes_coll = "shapes"
        self.classification_coll = "classification"

    def start_classification(self, request_data):
        user_id = request_data.user_id
        map_id = request_data.map_id
        reset = request_data.reset
        try:
            cache_id = f"{user_id}_{map_id}"

            cache_exists = self.cache.hexists(name=cache_id, key='features')
            if cache_exists and not reset:
                features = json.loads(self.cache.hget(name=cache_id, key='features'))
                current_feature = int(self.cache.hget(name=cache_id, key='current_feature'))
                classified_features = json.loads(self.cache.hget(name=cache_id, key='classified_features'))
                this_feature = features[current_feature]
                total_features = len(features)
            else:
                map_features = self.conn.find_one(database_name=self.db_name,
                                                  collection_name=self.shapes_coll,
                                                  query=dict(map_id=map_id))
                LOG.debug(f"Queried the features for map with id {map_id}")
                features = map_features["content"]["features"]
                LOG.trace(f"Features: {features}")
                pages = len(features) / 10
                classified_features = list()
                current_feature = 0
                LOG.trace(f"Pages for pagination: {pages}")
                user_classification_cache = dict(features=json.dumps(features),
                                                 pages=pages,
                                                 current_page=0,
                                                 current_feature=0,
                                                 classified_features=json.dumps(classified_features))
                total_features = len(features)
                LOG.trace(f"Total features: {total_features}")
                this_feature = features[0]
                LOG.trace(f"This feature: {this_feature}")
                self.cache.hset(name=cache_id,
                                mapping=user_classification_cache)
                LOG.debug(f"Stored the classification user session in cache")
            return dict(total_features=total_features,
                        classified=classified_features,
                        feature=this_feature,
                        current_feature=current_feature)
        except Exception as e:
            raise Exception(f"Faced to start classification session for map {map_id} for user {user_id}: {e}")

    def get_next_feature(self, request_data):
        user_id = request_data.user_id
        map_id = request_data.map_id
        current_feature = request_data.current_feature
        save = request_data.save
        content = request_data.content
        try:
            cache_id = f"{user_id}_{map_id}"
            # current_feature = int(self.cache.hget(name=cache_id, key='current_feature'))

            # current_page = user_classification_cache["current_page"]
            # current_feature = user_classification_cache["current_feature"]
            # if current_feature == 9:
            #     user_classification_cache["current_page"] = current_page + 1
            #     user_classification_cache["current_feature"] = 0
            # else:

            if save:
                save_req = SaveFeatureClassificationRequest
                save_req.user_id = user_id
                save_req.map_id = map_id
                save_req.feature_index = current_feature
                save_req.content = content
                self.save_feature_details(save_req)

            current_feature += 1
            self.cache.hset(name=cache_id,
                            key='current_feature',
                            value=current_feature)
            req = FeatureByIndexRequest
            req.user_id = user_id
            req.map_id = map_id
            req.feature_index = current_feature
            return self.get_feature_by_index(request_data=req)
        except Exception as e:
            raise Exception(f"Faced an issue when fetching the next classification: {e}")

    def get_feature_by_index(self, request_data):
        user_id = request_data.user_id
        map_id = request_data.map_id
        feature_index = request_data.feature_index
        try:
            content = None
            cache_id = f"{user_id}_{map_id}"
            features = json.loads(self.cache.hget(name=cache_id, key='features'))
            classified_features = json.loads(self.cache.hget(name=cache_id, key='classified_features'))

            if feature_index > len(features) - 1:
                feature_index = len(features) - 1

            this_feature = features[feature_index]
            total_features = len(features)

            feature_id = features[feature_index]["properties"]["class"]
            res = self.conn.find_one(database_name=self.db_name,
                                     collection_name=self.classification_coll,
                                     query=dict(user_id=user_id,
                                                map_id=map_id,
                                                feature_id=feature_id))

            if res is not None:
                content = res["content"]
            classified_features = list(set(classified_features))
            return dict(total_features=total_features,
                        classified=classified_features,
                        feature=this_feature,
                        current_feature=feature_index,
                        content=content)
        except Exception as e:
            raise Exception(f"Faced an issue when fetching feature by id: {e}")

    def save_feature_details(self, request_data):
        user_id = request_data.user_id
        map_id = request_data.map_id
        feature_index = request_data.feature_index
        content = request_data.content
        try:
            cache_id = f"{user_id}_{map_id}"
            classified_features = json.loads(self.cache.hget(name=cache_id, key='classified_features'))
            features = json.loads(self.cache.hget(name=cache_id, key='features'))
            feature_id = features[feature_index]["properties"]["class"]

            self.conn.update_one(database_name=self.db_name,
                                 collection_name=self.classification_coll,
                                 query=dict(user_id=user_id,
                                            map_id=map_id,
                                            feature_id=feature_id),
                                 data=dict(content=content),
                                 upsert=True)
            classified_features.append(feature_index)
            classified_features = list(set(classified_features))
            self.cache.hset(name=cache_id,
                            key='classified_features',
                            value=json.dumps(classified_features))
            return True
        except Exception as e:
            raise Exception(f"Faced an issue when saving classification details: {e}")

    def get_classified_features(self, user_id, map_id):
        try:
            cache_id = f"{user_id}_{map_id}"
            classified_features = json.loads(self.cache.hget(name=cache_id, key='classified_features'))
            return classified_features
        except Exception as e:
            raise Exception(f"Faced an issue when fetching classified features: {e}")
