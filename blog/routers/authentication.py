from fastapi.security import OAuth2PasswordRequestForm
from JWTtoken import create_access_token
from schemas import Login
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
import models
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {request.username} not found"
        )
    if not pwd_cxt.verify(request.password , user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password"
        )
        
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    #generate jwt token
    
    # return user


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
