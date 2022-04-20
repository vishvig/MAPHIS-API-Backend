from ..endpoints import *
from ..handlers.user import UserHandler
from ..models.endpoints.response import *
from ..models.endpoints.request.user import *

from exceptions.users.error_codes import *

module = "user"
router = APIRouter(prefix=api(module))
tags = [module]
handler = UserHandler()


@router.post('/add', tags=tags)
async def add_user(request_data: AddUserRequest):
    try:
        response_json = handler.add_user(request_data=request_data)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.delete('/{userid}', tags=tags)
async def delete_user(userid: str):
    try:
        response_json = handler.delete_user(userid)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/update', tags=tags)
async def update_user(request_data: UpdateUserRequest):
    try:
        response_json = handler.update_user(request_data=request_data)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/{userid}', tags=tags)
async def get_user(userid: str):
    try:
        response_json = handler.get_user(userid)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
