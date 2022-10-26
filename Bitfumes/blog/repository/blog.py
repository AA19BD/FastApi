from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..schemas import Blog, UpdatedBlog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, blog: Blog):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Id {blog_id} was not found!')

    db.commit()
    return {"Data": f"{blog_id} was removed!"}


def show(blog_id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='The Blog doesnt exist!')
        # response.status_code = status.HTTP_404_NOT_FOUND
    return blogs


def update(blog_id: int, blog: UpdatedBlog, db: Session):
    blog_ = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Id {blog_id} was not found!')
    if blog.title:
        blog_.title = blog.title
    if blog.body:
        blog_.body = blog.body
    db.commit()
    return blog_