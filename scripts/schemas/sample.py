from typing import Dict, Optional, List, Any, Union

from pydantic import BaseModel


class ReturnTextRequest(BaseModel):
    text: str


class TwoNumberCalculatorRequest(BaseModel):
    num_1: str
    num_2: str
    expression: str
