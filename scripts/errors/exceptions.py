class MaphisException(Exception):
    pass


class DbException(MaphisException):
    pass


class UserAlreadyExistsException(MaphisException):
    pass
