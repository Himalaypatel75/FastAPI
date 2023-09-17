# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# # path variable Example
# @app.get("/user/{user}")
# async def index(user: int):
#     return {"data": {"name": user}}


# # query parameter variable Example
# @app.get("/query")
# async def query_get(limit: int = 10, sort: Optional[str] = None):
#     return {"data": {"limit": limit}}


# class Blog(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[int] = None


# # post methord
# @app.post("/blog")
# async def create_blog(blog: Blog):
#     # print(blog.name)
#     return {"data": blog}
