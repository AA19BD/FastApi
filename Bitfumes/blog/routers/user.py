from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from ..schemas import User, ShowUser
from ..database import get_db
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(user_: User, db: Session = Depends(get_db)):
    return user.create(user_, db)


@router.get('/{user_id}',status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(user_id:int, db: Session = Depends(get_db)):
    return user.get(user_id, db)
