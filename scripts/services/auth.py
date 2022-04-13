from fastapi import APIRouter, HTTPException

from scripts.schemas.auth import Token, LoginRequest

from scripts.core.handlers.user import UserHandler
from scripts.core.handlers.auth import create_access_token

auth_router = APIRouter()


@auth_router.post('/auth', response_model=Token)
def authenticate_user(request: LoginRequest):
    """
    Function responsible for authenticating user and returning the access token

    Args:
        request(LoginRequest): an object containing user email and password

    Returns:
        Access token and token type
    """
    user = UserHandler()
    user_valid = user.validate_user(request.email, request.password)
    if not user_valid:
        raise HTTPException(status_code=401, detail='Email or password entered is incorrect')
    # fetch the user detail
    user_details = user.get_user(email=request.email)
    access_token = create_access_token(user_details['details'])
    return {'access_token': access_token, 'token_type': 'Bearer'}
