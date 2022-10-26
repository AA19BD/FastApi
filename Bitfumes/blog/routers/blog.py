from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List

from ..schemas import ShowBlog, Blog, UpdatedBlog
from ..database import get_db
from ..repository import blog
from ..schemas import User
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def all(db: Session = Depends(get_db), get_current_user: User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blog_: Blog, db: Session = Depends(get_db)):
    return blog.create(db, blog_)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(*, blog_id: int, db: Session = Depends(get_db), response: Response):
    return blog.show(blog_id, db)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(blog_id: int, db: Session = Depends(get_db)):
    return blog.destroy(blog_id, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update(blog_id: int, blog_: UpdatedBlog, db: Session = Depends(get_db)):
    return blog.update(blog_id, blog_, db)
