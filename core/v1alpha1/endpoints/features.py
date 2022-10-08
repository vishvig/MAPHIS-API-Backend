from ..endpoints import *
from ..handlers.features import FeatureHandler

from ..models.endpoints.request.features import *

from exceptions.features.error_codes import *
from exceptions.features.exceptions import MapFeatureAlreadyExistsException, FeaturesException,\
    UnknownInsertQueryException


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


@router.post('/upload/images/{map_id}/{z}/{x}/{y}', tags=tags)
async def start_feature_classification(map_id, z, x, y, file: UploadFile = File(...)):
    """
    Endpoint to upload map/region tiles(images) after segmentation

    Args:
        map_id: ID of the map/region to which the tile belongs to
        x: The x co-ordinate of the tile (upper left corner)
        y: The y co-ordinate of the tile (upper left corner)
        z: The zoom level of the tile/image
        file: A bytes type object of the image

    Returns:
        Boolean status of file upload
    """
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


@router.post('/{map_id}/{feature_class}/insert/{insert_type}', tags=tags)
async def upload_map_features(map_id, feature_class, insert_type, request_data: FeatureCollection):
    """
    Endpoint to upload geoJSON metadata of the classified features

    Args:
        map_id: ID of the map/region to which the feature belongs to
        feature_class: The feature class that the feature belongs to
        insert_type: Supported values - append/replace
        request_data(FeatureCollection): GeoJSON metadata of all the classified features

    Returns:
        Status of upload operation
    """
    try:
        res = handler.upload_feature_list(feature_collection=request_data,
                                          map_id=map_id,
                                          feature_class=feature_class,
                                          insert_type=insert_type)
        return JSONResponse(content=res)
    except UnknownInsertQueryException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/{map_id}/{feature_class}', tags=tags)
async def get_map_features(map_id, feature_class):
    """
    Fetch the features belonging to a particular class in a particular region

    Args:
        map_id: ID of the map/region to which the feature belongs to
        feature_class: The feature class that the feature belongs to

    Returns:
        The GeoJSON metadata of the features belonging to the queried feature class and region
    """
    try:
        res = handler.get_map_features(map_id=map_id, feature_class=feature_class)
        return JSONResponse(content=res)
    except MapFeatureAlreadyExistsException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
