from typing import List
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
from database import get_db
from schemas import Blog, ShowBlogTitle, User, ShowUser, CreateBlog
import models
from database import engine
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter( tags=["User"], prefix="/user")

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("")
def create_user(request: User, db: Session = Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(
        name=request.name, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    "/all-user",
    status_code=status.HTTP_201_CREATED,
    response_model=List[ShowUser],
)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.User).all()
    return blogs
