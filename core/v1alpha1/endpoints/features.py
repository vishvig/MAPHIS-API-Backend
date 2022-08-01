from ..endpoints import *
from ..handlers.features import FeatureHandler

from ..models.endpoints.request.features import *

from exceptions.features.error_codes import *
from exceptions.features.exceptions import MapFeatureAlreadyExistsException

from constants.configurations import Service

module = "features"
router = APIRouter(prefix=api(module))
tags = [module]
handler = FeatureHandler()

# @router.get('/serve/dummy', tags=tags)
# async def serve_dummy_image():
#     try:
#         image, media_type = handler.serve_dummy_image()
#         return StreamingResponse(image, media_type=media_type)
#     except UserNotValidException as e:
#         raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
#     except MaphisException as e:
#         raise MaphisEndpointException(error_type=TYP001, message=e)
#     except Exception as e:
#         raise MaphisEndpointException(message=e)


@router.post('/upload/images/{map_id}/{x}/{y}/{z}', tags=tags)
async def start_feature_classification(map_id, x, y, z, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        res = handler.upload_single_image(map_id=map_id, x=x, y=y, z=z, contents=contents)
        return True
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


# @router.post('/upload/images/batch', tags=tags)
# async def start_feature_classification(request_data: MultipleImageUploadRequest, files: List[UploadFile] = File(...)):
#     try:
#         res = handler.upload_multiple_images(request_data=request_data, files=files)
#         return JSONResponse(content=res)
#     except MaphisException as e:
#         raise MaphisEndpointException(error_type=TYP001, message=e)
#     except Exception as e:
#         raise MaphisEndpointException(message=e)


@router.post('/features/{map_id}/insert', tags=tags)
async def upload_map_features(map_id, request_data: FeatureCollection):
    try:
        res = handler.upload_feature_list(feature_collection=request_data, map_id=map_id)
        return JSONResponse(content=res)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/features/{map_id}', tags=tags)
async def upload_map_features(map_id):
    try:
        res = handler.get_map_features(map_id=map_id)
        return JSONResponse(content=res)
    except MapFeatureAlreadyExistsException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
