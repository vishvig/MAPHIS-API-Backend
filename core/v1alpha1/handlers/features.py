import pandas as pd
import geopandas as gpd

from utils import *
from utils.mongo_util import mongo_conn
from utils.postgres_util import PostgresDBUtil
from utils.common_utils import CommonUtils

from constants.configurations import MongoDB, Service, PostgresDB

from exceptions.features.exceptions import *
from exceptions.features.error_codes import *

from shapely.geometry import shape


class FeatureHandler(object):
    def __init__(self):
        self._cu_ = CommonUtils()

        self.conn = mongo_conn
        self.db_name = MongoDB.name
        self.shapes_coll = "shapes"
        self.engine = PostgresDBUtil().engine()
        self.psql_schema = PostgresDB.schema

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

    def upload_feature_list(self, map_id, feature_collection, feature_class, insert_type):
        try:
            db_data = dict(id=list(),
                           map=list(),
                           geometry=list())
            feature_collection_ids = dict(type=feature_collection.type,
                                          features=list())
            for i, feature in enumerate(feature_collection.features):
                _feature = dict(type='Feature',
                                properties=feature.properties,
                                geometry=feature.geometry)
                _id = self._cu_.generate_random_id()
                _feature['properties']['id'] = _id
                feature_collection_ids['features'].append(_feature)
                db_data['id'].append(_id)
                db_data['map'].append(map_id)
                db_data['geometry'].append(shape(_feature['geometry']))
            df = pd.DataFrame(db_data)
            gdf = gpd.GeoDataFrame(df, crs="EPSG:4326")
            data = self.conn.find_one(database_name=self.db_name,
                                      collection_name=self.shapes_coll,
                                      query=dict(map_id=map_id, feature_class=feature_class),
                                      filter_dict={})
            if insert_type == 'replace':
                if data is None:
                    _id = self._cu_.generate_random_id()
                else:
                    _id = data['_id']
                data = dict(_id=_id,
                            map_id=map_id,
                            feature_class=feature_class,
                            content=feature_collection_ids)
                gdf.to_postgis(feature_class,
                               self.engine,
                               schema=self.psql_schema,
                               index=False,
                               if_exists='replace')
            elif insert_type == 'append':
                data['content']['features'].extend(feature_collection_ids['features'])
                gdf.to_postgis(feature_class,
                               self.engine,
                               schema=self.psql_schema,
                               index=False,
                               if_exists='append')
            else:
                raise UnknownInsertQueryException
            self.conn.update_one(database_name=self.db_name,
                                 collection_name=self.shapes_coll,
                                 data=data,
                                 query=dict(map_id=map_id, feature_class=feature_class),
                                 upsert=True)
            return True
        except UnknownInsertQueryException:
            raise UnknownInsertQueryException
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise FeaturesException(e)

    def get_map_features(self, map_id, feature_class):
        data = self.conn.find_one(database_name=self.db_name,
                                  collection_name=self.shapes_coll,
                                  query=dict(map_id=map_id, feature_class=feature_class))
        return data['content']
