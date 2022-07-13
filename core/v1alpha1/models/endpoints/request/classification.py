from ....models import *


class StartClassifyRequest(BaseModel):
    user_id: str
    map_id: str
    reset: bool = False


class NextFeatureRequest(BaseModel):
    user_id: str
    map_id: str
    current_feature: int
    save: bool = False
    content: Optional[Dict] = dict()


class FeatureByIndexRequest(BaseModel):
    user_id: str
    map_id: str
    feature_index: int


class SaveFeatureClassificationRequest(BaseModel):
    user_id: str
    map_id: str
    feature_index: int
    content: Optional[Dict] = dict()
