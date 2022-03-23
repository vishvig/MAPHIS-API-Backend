from typing import Optional, Any

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: str = "Failed"
    message: Optional[str]
    data: Optional[Any]


class DefaultFailureResponse(DefaultResponse):
    error: Any
