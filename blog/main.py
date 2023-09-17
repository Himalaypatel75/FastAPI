from fastapi import FastAPI
from  schemas import Blog
import models
from database import engine

models.Base.metadata.create_all(engine)

blog_app = FastAPI()

# post methord
@blog_app.post("/blog")
async def create_blog(blog: Blog):
    # print(blog.name)
    return {"data": blog}
