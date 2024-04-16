from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.users import Users
from schemas.User import (
    User as UserSchema,
    UserBase as UserBaseSchema,
    UserCreate as UserCreateSchema,
)
from services import users as user_service
from logger import logger


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    try:
        users = user_service.get_users(db)
        return users
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to get users")


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = user_service.get_user(user_id, db)
        return {"message": "User retrieved successfully", "data": user}
    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to get user")


@router.post("/create")
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    try:
        user = user_service.create_user(user, db)
        return {"message": "Successfully Created User", "data": user}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to save user")


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_service.delete_user(user_id, db)
        return {"message": "Successfully Deleted User"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete user")
