from typing import List
from routers import blog, user, authentication
from fastapi import FastAPI, Depends, HTTPException, Response, status
from database import get_db
from schemas import Blog, ShowBlogTitle, User, ShowUser
import models
from database import engine
from sqlalchemy.orm import Session, relationship
from passlib.context import CryptContext

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
