from exceptions.db.redis import RedisException


class RedisConnectionException(RedisException):
    pass


class RedisHSetException(RedisException):
    pass


class RedisHGetException(RedisException):
    pass
