from typing import Dict, Optional, List, Any, Union

from pydantic import BaseModel


class AddUserRequest(BaseModel):
    username: str
    password: str
    details: Optional[Dict] = dict()


class DeleteUserRequest(BaseModel):
    userid: str


class UpdateUserRequest(BaseModel):
    userid: str
    password: Optional[Any] = None
    details: Optional[Dict] = None


class GetUserRequest(BaseModel):
    userid: str
