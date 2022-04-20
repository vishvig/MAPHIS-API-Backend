from constants.constants import Encryption
from utils.common_utils import CommonUtils
from exceptions.users.exceptions import *

from ..handlers.user import UserHandler


class AuthHandler(object):
    def __init__(self):
        self._cu_ = CommonUtils()
        self._uh_ = UserHandler()

    def create_access_token(self, request):
        """
        function to generate encoded access token, then to be used by the UI.

        Args:
            request(UserDetails): These are user details which are stored in the DB

        Returns:
            encoded_jwt(str): an encrypted JWT

        Notes:
             for more information on JWT please take a look at https://jwt.io
        """
        try:
            user_valid = self._uh_.validate_user(request.email, request.password)
            if not user_valid:
                raise UserNotValidException(request.email)
            user_details = self._uh_.get_user(email=request.email)
            to_encode = user_details['details'].copy()
            expire = self._cu_.get_utc_datetime_now() + self._cu_.get_timedelta('weeks', 3)
            to_encode.update({'exp': expire})
            encoded_jwt = self._cu_.jwt_encode(to_encode, Encryption.api_secret_key, algorithm=Encryption.algorithm)
            return encoded_jwt
        except UserNotValidException as e:
            raise UserNotValidException(e)
        except Exception as e:
            raise Exception(f"Faced an issue when creating an access token for the user: {e}")

    def decode_access_token(self, token: str):
        """
        Function to decode access token

        Args:
             token(str): encrypted token to be decrypted

        Returns:
            decoded data object
        """
        try:
            return self._cu_.jwt_decode(token, Encryption.api_secret_key, Encryption.algorithm)
        except Exception as e:
            raise Exception(f"Faced an issue when decoding the access token: {e}")
