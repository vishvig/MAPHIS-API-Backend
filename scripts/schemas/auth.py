from typing import Dict, Optional, List, Any, Union

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str
