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
    """
    Endpoint to start feature classification session for a user

    Args:
        request_data(StartClassifyRequest): Object to start/restart the classification

    Returns:
        Object containing information about the total features, classified features and current feature to be classified
    """
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
    """
    Endpoint to move to the next feature to classify

    Args:
        request_data(NextFeatureRequest): Object containing the current feature id,
         content of current classified feature and a boolean value to indicate if the current classification to be saved

    Returns:
        Object containing information about the total features, classified features and current feature to be classified
    """

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
    """
    Endpoint to get a feature by its id

    Args:
        request_data(FeatureByIndexRequest): Object containing the feature index

    Returns:
        Object containing information about the total features, classified features and current feature to be classified
    """
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
    """
    Endpoint to save a classified feature

    Args:
        request_data(SaveFeatureClassificationRequest): Object containing the feature index and
        the classification content

    Returns:
        Status of saving the feature
    """
    try:
        res = handler.save_feature_details(request_data=request_data)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/feature/classified', tags=tags)
async def get_classified_features(user_id: str, map_id: str):
    """
    Endpoint to get the list of all classified features

    Args:
        user_id: The id of the user whose classification session needs to be retrieved
        map_id: The id of the map/region

    Returns:
        Object containing all list of all classified features
    """
    try:
        res = handler.get_classified_features(user_id=user_id, map_id=map_id)
        return JSONResponse(content=res)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
