from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.users import User
from schemas.User import User as UserSchema
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
        users = user_service.get(db)
        return users
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to get users")


@router.get("/:user_id")
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = user_service.get_user(user_id, db)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
