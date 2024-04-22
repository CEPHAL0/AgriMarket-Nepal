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
from services.index import auth as auth_service


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

    if len(user.password) < 8:
        raise HTTPException(
            status_code=400, detail="Password must be at least 8 characters long"
        )

    hashed_password = auth_service.get_password_hash(user.password)

    db_user = Users(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hashed_password,
        image=user.image,
        role=RoleEnum.USER,
        address=user.address,
        phone=user.phone,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(id: int, user: UserCreateSchema, db: Session):
    db_user: Users = db.query(Users).filter(Users.id == id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_username = get_user_by_username(user.username, db)

    if (user_username is not None) and (user_username.id != id):
        raise HTTPException(status_code=400, detail="Username already taken")

    user_email = get_user_by_email(user.email, db)

    if (user_email is not None) and (user_email.id != id):
        raise HTTPException(status_code=400, detail="Email already taken")

    user_phone = get_user_by_phone_number(user.phone, db)

    if (user_phone is not None) and (user_phone.id != id):
        raise HTTPException(status_code=400, detail="Phone Number already taken")

    if len(user.password) < 8:
        raise HTTPException(
            status_code=400, detail="Password should be at least 8 characters long"
        )

    hashed_password = auth_service.get_password_hash(user.password)

    db_user.name = user.name
    db_user.email = user.email
    db_user.address = user.address
    db_user.image = user.image
    db_user.role = user.role
    db_user.phone = user.phone
    db_user.username = user.username
    db_user.password = hashed_password

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = db.query(Users).filter(Users.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
