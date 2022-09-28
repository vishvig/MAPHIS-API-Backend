from ....models import *


class SingleImageUploadRequest(BaseModel):
    map_id: Any
    x: Any
    y: Any
    z: Any


class MultipleImageUploadRequest(BaseModel):
    metadata: List[SingleImageUploadRequest]


class Feature(BaseModel):
    type: Any = 'Feature'
    properties: Dict
    geometry: Dict


class FeatureCollection(BaseModel):
    type: Any = 'FeatureCollection'
    features: List[Feature]


class FeatureCollectionRequest(BaseModel):
    features: FeatureCollection
