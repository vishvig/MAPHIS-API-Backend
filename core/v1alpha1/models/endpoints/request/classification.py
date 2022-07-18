from ....models import *


class ClassifyBaseModel(BaseModel):
    user_id: str
    map_id: str


class StartClassifyRequest(ClassifyBaseModel):
    reset: bool = False


class NextFeatureRequest(ClassifyBaseModel):
    current_feature: int
    save: bool = False
    content: Optional[Dict] = dict()


class FeatureByIndexRequest(ClassifyBaseModel):
    feature_index: int


class SaveFeatureClassificationRequest(ClassifyBaseModel):
    feature_index: int
    content: Optional[Dict] = dict()


class FetchClassifiedFeatures(ClassifyBaseModel):
    pass
