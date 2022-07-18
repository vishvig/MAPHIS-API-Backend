from ..endpoints import *
from ..handlers.classification import ClassifyHandler

from ..models.endpoints.request.classification import *

from exceptions.users.error_codes import *
from exceptions.users.exceptions import UserNotValidException

module = "classification"
router = APIRouter(prefix=api(module))
tags = [module]
handler = ClassifyHandler()


@router.post('/start', tags=tags)
async def start_feature_classification(request_data: StartClassifyRequest):
    try:
        res = handler.start_classification(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/feature/next', tags=tags)
async def get_next_feature(request_data: NextFeatureRequest):
    try:
        res = handler.get_next_feature(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/feature/id', tags=tags)
async def get_feature_by_id(request_data: FeatureByIndexRequest):
    try:
        res = handler.get_feature_by_index(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/feature/save', tags=tags)
async def save_feature_by_id(request_data: SaveFeatureClassificationRequest):
    try:
        res = handler.save_feature_details(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/feature/classified', tags=tags)
async def get_classified_features(request_data: FetchClassifiedFeatures):
    try:
        res = handler.get_classified_features(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
