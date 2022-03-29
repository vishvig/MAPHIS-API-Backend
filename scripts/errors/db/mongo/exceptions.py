from scripts.errors.db.mongo import MongoException


class MongoConnectionException(MongoException):
    pass


class MongoQueryException(MongoException):
    pass
