import os

from utils import *
from utils.mongo_util import mongo_conn

from constants.configurations import MongoDB, Service

from exceptions.features.exceptions import *


class MetadataHandler(object):
    def __init__(self):
        self.conn = mongo_conn
        self.db_name = MongoDB.name
        self.shapes_coll = "shapes"

    @staticmethod
    def get_maps():
        try:
            maps = os.listdir(Service.images_path)
            return maps
        except Exception as e:
            return e

    def get_feature_classes(self):
        try:
            data = self.conn.distinct(database_name=self.db_name,
                                      collection_name=self.shapes_coll,
                                      query_key="feature_class")
            return data
        except Exception as e:
            return e
