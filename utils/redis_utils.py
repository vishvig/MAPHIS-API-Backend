import redis

from constants.configurations import CacheDB

from exceptions.db.redis.exceptions import *
from exceptions.db.redis.error_codes import *


class RedisUtils(object):
    def __init__(self):
        try:
            self.client = redis.Redis(host=CacheDB.host,
                                      port=CacheDB.port,
                                      db=CacheDB.db_name)
        except Exception as e:
            raise RedisConnectionException(REDIS001.format(e))

    def hset(self, name, key=None, value=None, mapping=None):
        try:
            res = self.client.hset(name=name, key=key, value=value, mapping=mapping)
            return res
        except Exception as e:
            raise RedisHSetException(REDIS002.format(f'Unable to set the hash name "{name}": {e}'))

    def hget(self, name, key):
        try:
            res = self.client.hget(name=name, key=key)
            return res
        except Exception as e:
            raise RedisHGetException(REDIS002.format(f'Unable to get the key {key} for hash name "{name}": {e}'))

    def hgetall(self, name):
        try:
            res = self.client.hgetall(name=name)
            return res
        except Exception as e:
            raise RedisHGetException(REDIS002.format(f'Unable to get the hash name "{name}": {e}'))

    def hexists(self, name, key):
        try:
            res = self.client.hexists(name=name, key=key)
            return res
        except Exception as e:
            raise RedisHGetException(REDIS002.format(f'Failed when checking for key {key} in name "{name}": {e}'))
