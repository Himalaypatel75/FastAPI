from schemas import Login
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
import models

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {request.username} not found"
        )
    return user


# # post methord
# @router.post("/blog")
# async def create_blog(request: CreateBlog, db: Session = Depends(get_db)):
#     # print(blog.name)
#     new_blog = models.Blog(
#         title=request.title, body=request.body, user_id=request.user_id
#     )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return {"data": new_blog}
