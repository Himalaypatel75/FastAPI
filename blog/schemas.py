from pydantic import BaseModel, EmailStr
from typing import List, Optional

# this pydentic model we used for serializing data


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class Blog(BaseModel):
    id: Optional[int] = None
    title: str
    body: Optional[str] = None
    user_id: Optional[int] = None
    creator: User


class CreateBlog(BaseModel):
    id: Optional[int] = None
    title: str
    body: Optional[str] = None
    user_id: Optional[int] = None


class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog]

    class Config:
        from_attributes = True


class ShowBlogTitle(BaseModel):
    # class ShowBlogTitle(Blog):
    title: str
    body: Optional[str] = None
    creator: User

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str
    # class Config:
    #     from_attributes = True
