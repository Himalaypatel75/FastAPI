from typing import List
from fastapi import FastAPI, Depends, HTTPException, Response, status, APIRouter
from database import get_db
from schemas import Blog, ShowBlogTitle, User, ShowUser, CreateBlog
import models
from database import engine
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/all-blog", status_code=status.HTTP_201_CREATED, response_model=List[ShowBlogTitle]
)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# post methord
@router.post("/blog")
async def create_blog(request: CreateBlog, db: Session = Depends(get_db)):
    # print(blog.name)
    new_blog = models.Blog(
        title=request.title, body=request.body, user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": new_blog}


@router.delete("/blog/{id}")
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found"
        )

    blog.delete(synchronize_session=False)
    db.commit()
    return {"data": f"{id} - id blog is deleted!"}


@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlogTitle)
def get_blog(id, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"data": f"no data found for {id}"},
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data": f"no data found for {id}"}
    return blogs


@router.put("/blog/{id}", status_code=status.HTTP_200_OK)
def update_blog(id, request: Blog, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    # blogs = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blogs:
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"data": f"no data found for {id}"},
        )
    blogs.title = request.title
    blogs.body = request.body
    # blogs.update({'title' : response.title, 'body' : response.body})
    db.commit()
    db.refresh(blogs)
    return blogs
