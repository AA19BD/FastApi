from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException, status
from models import User, Gender, Role, UpdatedUser


app = FastAPI() #Instance of Application


db: List[User] = [
    User(
        id=UUID("3cc404c3-8b94-4ec4-a5b7-a058b718d9c2"),
        first_name='Jamila',
        last_name='Ahmed',
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("1f75cf5b-7fd2-4243-8215-cbb5938a6e03"),
        first_name='Alex',
        last_name='Jones',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get('/')
async def root():
    return  {'Hello': 'World'}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return user


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f'User with id: {user_id} was deleted')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No such user!')


@app.put('/api/v1/users/{user_id}')
async def update_user(user_id: UUID, user: UpdatedUser):
    for user_ in db:
        if user_.id == user_id:
            if user.first_name:
                user_.first_name = user.first_name
            if user.last_name:
                user_.last_name = user.last_name
            if user.middle_name:
                user_.middle_name = user.middle_name
            if user.gender:
                user_.gender = user.gender
            if user.roles:
                user_.roles = user.roles
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f'User with id: {user_id} was updated!')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No such user!')
