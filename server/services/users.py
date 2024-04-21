from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.users import Users
from schemas import index
from schemas.Users import (
    User as UserSchema,
    UserBase as UserBaseSchema,
    UserCreate as UserCreateSchema,
)
from config.enums.role import RoleEnum


def get_user(user_id: int, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_username(username: str, db: Session):
    user = db.query(Users).filter(Users.username == username).first()
    # if user is None:
    #     raise HTTPException(status_code=404, detail="User with provided username not found")
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    # if user is None:
    #     raise HTTPException(status_code=404, detail="User with provided email not found")
    return user


def get_user_by_phone_number(phone_number: str, db: Session):
    user = db.query(Users).filter(Users.phone == phone_number).first()
    return user


def get_users(db: Session) -> list[UserSchema]:
    users = db.query(Users).all()
    return users


def create_user(user: UserCreateSchema, db: Session):

    db_user = Users(
        name=user.name,
        username=user.username,
        email=user.email,
        password=user.password,
        image=user.image,
        role=RoleEnum.USER,
        address=user.address,
        phone=user.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = db.query(Users).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
