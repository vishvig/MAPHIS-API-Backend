import os

from utils import *

from constants.configurations import Service

from exceptions.features.exceptions import *


class MetadataHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def get_maps():
        try:
            maps = os.listdir(Service.images_path)
            return maps
        except Exception as e:
            return e

    @staticmethod
    def get_feature_classes():
        try:
            return ['imprint', 'text', 'vegetation']
        except Exception as e:
            return e
