from exceptions.users import UsersException
from exceptions.users.error_codes import *


class UserAlreadyExistsException(UsersException):
    pass


class UserNotValidException(UsersException):
    def __init__(self, user):
        self.err_type = TYP002
        self.err_msg = USR002.format(user)
