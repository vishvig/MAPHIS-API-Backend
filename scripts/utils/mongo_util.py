"""
Mongo Utility
Author: Vignesh Ravishankar
Reference: Pymongo Documentation
"""
from typing import Dict, List, Optional

from pymongo import MongoClient

from scripts.constants.configurations import Db

from scripts.errors.db.mongo.exceptions import *
from scripts.errors.db.mongo.error_codes import *


class MongoCollectionClass:
    @property
    def key_mongo_default_id(self):
        return "_id"


class MongoConnect(object):
    def __init__(self, hosts, username, password, auth_db):
        try:
            self.client = MongoClient(hosts,
                                      username=username,
                                      password=password,
                                      ssl=False,
                                      connect=True,
                                      authSource=auth_db)
        except Exception as e:
            raise MongoConnectionException(MONGO001.format(e))

    def __del__(self):
        self.client.close()

    def insert_one(self, database_name: str, collection_name: str, data: Dict):
        """
        The function is used to inserting a document to a collection in a Mongo Database.
        :param database_name: Database Name
        :param collection_name: Collection Name
        :param data: Data to be inserted
        :return: Insert ID
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.insert_one(data)
            return response.inserted_id
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def insert_many(
        self, database_name: str, collection_name: str, data: List
    ):
        """
        The function is used to inserting documents to a collection in a Mongo Database.
        :param database_name: Database Name
        :param collection_name: Collection Name
        :param data: List of Data to be inserted
        :return: Insert IDs
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.insert_many(data)
            return response.inserted_ids
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def find(
        self,
        database_name: str,
        collection_name: str,
        query: Dict,
        filter_dict: Optional[Dict] = None,
        sort=None,
        skip: Optional[int] = 0,
        limit: Optional[int] = None,
    ):
        """
        The function is used to query documents from a given collection in a Mongo Database
        :param database_name: Database Name
        :param collection_name: Collection Name
        :param query: Query Dictionary
        :param filter_dict: Filter Dictionary
        :param sort: List of tuple with key and direction. [(key, -1), ...]
        :param skip: Skip Number
        :param limit: Limit Number
        :return: List of Documents
        """
        if sort is None:
            sort = list()
        if filter_dict is None:
            filter_dict = {"_id": 0}
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            if len(sort) > 0:
                cursor = (
                    collection.find(query, filter_dict).sort(sort).skip(skip)
                )
            else:
                cursor = collection.find(query, filter_dict).skip(skip)
            if limit:
                cursor = cursor.limit(limit)
            response = list(cursor)
            cursor.close()
            return response
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def find_one(
        self,
        database_name: str,
        collection_name: str,
        query: Dict,
        filter_dict: Optional[Dict] = None,
    ):
        try:
            if filter_dict is None:
                filter_dict = {"_id": 0}
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.find_one(query, filter_dict)
            return response
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def update_one(
        self,
        database_name: str,
        collection_name: str,
        query: Dict,
        data: Dict,
        upsert: bool = False,
    ):
        """

        :param upsert:
        :param database_name:
        :param collection_name:
        :param query:
        :param data:
        :return:
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.update_one(
                query, {"$set": data}, upsert=upsert
            )
            return response.modified_count
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def delete_many(
        self, database_name: str, collection_name: str, query: Dict
    ):
        """

        :param database_name:
        :param collection_name:
        :param query:
        :return:
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.delete_many(query)
            return response.deleted_count
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def delete_one(
        self, database_name: str, collection_name: str, query: Dict
    ):
        """

        :param database_name:
        :param collection_name:
        :param query:
        :return:
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.delete_one(query)
            return response.deleted_count
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))

    def distinct(
        self,
        database_name: str,
        collection_name: str,
        query_key: str,
        filter_json: Optional[Dict] = None,
    ):
        """
        :param database_name:
        :param collection_name:
        :param query_key:
        :param filter_json:
        :return:
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.distinct(query_key, filter_json)
            return response
        except Exception as e:
            raise MongoQueryException(MONGO002.format(e))


mongo_conn = MongoConnect(hosts=Db.mongo_db_host,
                          username=Db.mongo_db_user,
                          password=Db.mongo_db_password,
                          auth_db=Db.mongo_db_auth_db)
