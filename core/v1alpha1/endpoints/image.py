from ..endpoints import *
from ..handlers.image import ImageHandler

from exceptions.users.error_codes import *
from exceptions.users.exceptions import UserNotValidException

module = "image"
router = APIRouter(prefix=api(module))
tags = [module]
handler = ImageHandler()


@router.get('/serve/dummy', tags=tags)
async def serve_dummy_image():
    try:
        image, media_type = handler.serve_dummy_image()
        return StreamingResponse(image, media_type=media_type)
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
