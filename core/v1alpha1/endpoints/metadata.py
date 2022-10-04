from ..endpoints import *
from ..handlers.metadata import MetadataHandler

from ..models.endpoints.request.features import *

from exceptions.features.error_codes import *
from exceptions.features.exceptions import MapFeatureAlreadyExistsException, FeaturesException,\
    UnknownInsertQueryException

module = "metadata"
router = APIRouter(prefix=api(module))
tags = [module]
handler = MetadataHandler()


@router.get('/maps', tags=tags)
async def get_maps():
    try:
        res = handler.get_maps()
        return JSONResponse(content=res)
    except UnknownInsertQueryException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/feature/classes', tags=tags)
async def get_feature_classes():
    try:
        res = handler.get_feature_classes()
        return JSONResponse(content=res)
    except UnknownInsertQueryException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
