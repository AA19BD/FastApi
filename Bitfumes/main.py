from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int, published: bool, sort: Optional[str] = None):
    return {'data': sort}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{blog_id}')
def show(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int):
    return {'data': 'comments'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': blog.title}