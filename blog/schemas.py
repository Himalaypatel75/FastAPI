from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    id : Optional[int] = None
    title: str
    body: Optional[str] = None

