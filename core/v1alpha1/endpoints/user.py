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
    """
        Endpoint to add a user on the MAPHIS system

        Args:
            request_data(AddUserRequest): an object containing user email and password

        Returns:
            Success/Failure of user addition
    """
    try:
        response_json = handler.add_user(request_data=request_data)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.delete('/{userid}', tags=tags)
async def delete_user(userid: str):
    """
        Endpoint to delete a user from the MAPHIS system

        Args:
            userid: The ID of the user to be removed

        Returns:
            Success/Failure of user deletion
    """
    try:
        response_json = handler.delete_user(userid)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.post('/update', tags=tags)
async def update_user(request_data: UpdateUserRequest):
    """
        Endpoint to update a user on the MAPHIS system

        Args:
            request_data(UpdateUserRequest): an object containing user id, password and other additional details

        Returns:
            Success/Failure of user update
    """
    try:
        response_json = handler.update_user(request_data=request_data)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)


@router.get('/{userid}', tags=tags)
async def get_user(userid: str):
    """
        Endpoint to get details of a user registered on the MAPHIS system

        Args:
            userid: The ID of the user to be removed

        Returns:
            Object containing user details
    """

    try:
        response_json = handler.get_user(userid)
        return JSONResponse(content=response_json)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
