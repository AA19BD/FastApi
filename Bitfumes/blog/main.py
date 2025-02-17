from fastapi import FastAPI

from . import models
from .database import engine
from .routers import blog, user, login


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)


















