from datetime import timedelta, datetime
import jwt
from scripts.schemas.user import UserDetails

secret_key = 'VSgqZfmtvsCzf8oGLjT660AfpVU2CGYb'
algorithm = 'HS256'


def create_access_token(*, data: UserDetails, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decode_access_token(*, data: str):
    return jwt.decode(data, secret_key, algorithm)


