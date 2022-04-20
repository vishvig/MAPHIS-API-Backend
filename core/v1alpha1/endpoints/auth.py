from ..endpoints import *
from ..handlers.auth import AuthHandler
from ..models.endpoints.response.auth import *

from exceptions.users.error_codes import *
from exceptions.users.exceptions import UserNotValidException

module = "auth"
router = APIRouter(prefix=api(module))
tags = [module]
handler = AuthHandler()


@router.post('/auth', response_model=Token, tags=tags)
def authenticate_user(request: LoginRequest):
    """
    Function responsible for authenticating user and returning the access token

    Args:
        request(LoginRequest): an object containing user email and password

    Returns:
        Access token and token type
    """
    try:
        access_token = handler.create_access_token(request=request)
        return {'access_token': access_token, 'token_type': 'Bearer'}
    except UserNotValidException as e:
        raise MaphisEndpointException(error_type=e.err_type, message=e.err_msg)
    except MaphisException as e:
        raise MaphisEndpointException(error_type=TYP001, message=e)
    except Exception as e:
        raise MaphisEndpointException(message=e)
