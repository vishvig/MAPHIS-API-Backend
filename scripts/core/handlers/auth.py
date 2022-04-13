from datetime import timedelta, datetime
import jwt
from scripts.schemas.user import UserDetails

secret_key = 'VSgqZfmtvsCzf8oGLjT660AfpVU2CGYb'
algorithm = 'HS256'


def create_access_token(data: UserDetails, expires_delta: timedelta = timedelta(minutes=15)):
    """
    function to generate encoded access token, then to be used by the UI.

    Args:
        data(UserDetails): These are user details which are stored in the DB
        expires_delta(timedelta): a timedelta object to set the expiry of token

    Returns:
        encoded_jwt(str): an encrypted JWT

    Notes:
         for more information on JWT please take a look at https://jwt.io
    """
    to_encode = data.copy()
    expire = datetime.utcnow()+expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decode_access_token(token: str):
    """
    Function to decode access token

    Args:
         token(str): encrypted token to be decrypted

    Returns:
        decoded data object
    """
    return jwt.decode(token, secret_key, algorithm)
