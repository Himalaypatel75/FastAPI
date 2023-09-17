from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[int] = None
