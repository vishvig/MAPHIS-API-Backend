from typing import Optional, Any

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: str = "Failed"
    message: Optional[str]
    data: Optional[Any]


class DefaultFailureResponse(DefaultResponse):
    error: Any


class ErrorException(Exception):
    """
    A class to create custom error exception

    Args:
        error_type(str): this is the error type generated like 'Internal server error'
        status(int): HTTP status code starts from 400
        message(Any): Error message if any, default is 'something went wrong'

    Notes:
        See https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
        for more info on creating custom error handlers
    """
    def __init__(self, error_type: str, status: int, message: Any = 'Something went wrong'):
        self.type = error_type
        self.message = message
        self.status = status

