from ....models import *


class AddUserRequest(BaseModel):
    email: str
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
