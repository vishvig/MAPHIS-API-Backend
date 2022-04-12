from scripts.utils.mongo_util import mongo_conn
from scripts.utils.common_utils import CommonUtils

from scripts.constants.configurations import Db

from scripts.errors.users.exceptions import *
from scripts.errors.users.error_codes import *


class UserHandler(object):
    def __init__(self):
        self._cu_ = CommonUtils()

        self.conn = mongo_conn
        self.db_name = Db.mongo_db_name
        self.collection_name = "users"

    def add_user(self, request_data):
        try:
            data = dict()
            mongo_data = self.conn.find_one(database_name=self.db_name,
                                            collection_name=self.collection_name,
                                            query=dict(username=request_data.email))
            if mongo_data is not None:
                raise UserAlreadyExistsException(USR001.format(request_data.email))
            _id = self._cu_.generate_random_id()
            data['_id'] = _id
            data['email'] = request_data.email
            data['password'] = request_data.password
            data['details'] = request_data.details
            self.conn.insert_one(database_name=self.db_name,
                                 collection_name=self.collection_name,
                                 data=data)
            return dict(userid=_id)
        except UserAlreadyExistsException as e:
            raise UserAlreadyExistsException(e)
        except Exception as e:
            raise Exception(f"Faced an issue when adding the user: {e}")

    def delete_user(self, userid):
        try:
            self.conn.delete_one(database_name=self.db_name,
                                 collection_name=self.collection_name,
                                 query=dict(_id=userid))
            return True
        except Exception as e:
            raise Exception(f"Faced an issue when deleting the user: {e}")

    def update_user(self, request_data):
        try:
            data = self.conn.find_one(database_name=self.db_name,
                                      collection_name=self.collection_name,
                                      query=dict(_id=request_data.userid))
            if request_data.password is not None:
                data["password"] = request_data.password
            if request_data.details is not None:
                data["details"].update(request_data.details)
            self.conn.update_one(database_name=self.db_name,
                                 collection_name=self.collection_name,
                                 query=dict(_id=request_data.userid),
                                 data=data)
            return True
        except Exception as e:
            raise Exception(f"Faced an issue when updating the user: {e}")

    def get_user(self, user_id):
        try:
            response = dict()
            data = self.conn.find_one(database_name=self.db_name,
                                      collection_name=self.collection_name,
                                      query=dict(_id=user_id))
            response["email"] = data["email"]
            response["details"] = data["details"]
            return response
        except Exception as e:
            raise Exception(f"Faced an issue when updating the user: {e}")
