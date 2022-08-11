from exceptions.features import FeaturesException
from exceptions.features.error_codes import *


class MapFeatureAlreadyExistsException(FeaturesException):
    def __init__(self, map_id):
        self.err_type = TYP001
        self.err_msg = FTR001.format(map_id)

