import copy
import os

from utils import *
from utils.mongo_util import mongo_conn
from utils.common_utils import CommonUtils

from constants.configurations import Db, Service

from exceptions.features.exceptions import *
from exceptions.features.error_codes import *


class FeatureHandler(object):
    def __init__(self):
        self._cu_ = CommonUtils()

        self.conn = mongo_conn
        self.db_name = Db.mongo_db_name
        self.shapes_coll = "shapes"

    # @staticmethod
    # def serve_dummy_image():
    #     # im = cv2.imread('dummy.tif', -1)
    #     # res, im_png = cv2.imencode(".png", im)
    #     im = cv2.imread('dummy.jpg', -1)
    #     print(io.TextIOWrapper(io.BytesIO(im.tobytes())))
    #     return io.TextIOWrapper(io.BytesIO(im.tobytes())), "image/jpg"

    @staticmethod
    def upload_single_image(map_id, x, y, z, contents):
        try:
            base_path = os.path.join(Service.images_path, map_id, x, y)
            try:
                os.makedirs(base_path)
            except OSError as e:
                pass
            with open(os.path.join(base_path, f'{z}.jpg'), 'wb') as f:
                f.write(contents)
            return True
        except Exception as e:
            return e

    # def upload_multiple_images(self, request_data, files):
    #     for i, file in enumerate(files):
    #         self.upload_single_image(request_data=request_data.metadata[i], _file=file)
    #     return True

    def upload_feature_list(self, map_id, feature_collection, feature_class):
        try:
            feature_collection_ids = dict(type=feature_collection.type,
                                          features=list())
            for i, feature in enumerate(feature_collection.features):
                _feature = dict(type='Feature',
                                properties=feature.properties,
                                geometry=feature.geometry)
                _feature['properties']['id'] = self._cu_.generate_random_id()
                feature_collection_ids['features'].append(_feature)
            existing_map = self.conn.find_one(database_name=self.db_name,
                                              collection_name=self.shapes_coll,
                                              query=dict(map_id=map_id, feature_class=feature_class))
            if existing_map is not None:
                raise MapFeatureAlreadyExistsException(map_id=map_id)
            else:
                data = dict(_id=self._cu_.generate_random_id(),
                            map_id=map_id,
                            feature_class=feature_class,
                            content=feature_collection_ids)
            self.conn.insert_one(database_name=self.db_name,
                                 collection_name=self.shapes_coll,
                                 data=data)
            return True
        except Exception as e:
            raise FeaturesException(e)

    def get_map_features(self, map_id, feature_class):
        data = self.conn.find_one(database_name=self.db_name,
                                  collection_name=self.shapes_coll,
                                  query=dict(map_id=map_id, feature_class=feature_class))
        return data['content']
