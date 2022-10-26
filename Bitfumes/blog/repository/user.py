from fastapi import  status, HTTPException, Depends
from sqlalchemy.orm import Session

from .. import models, hashing
from ..schemas import User
from ..database import get_db


def create(user: User, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email, password=hashing.Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='The user doesnt exist!')
    return user