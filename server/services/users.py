from sqlalchemy.orm import Session

from models import index as models
from schemas import index
from schemas.User import User as UserSchema


def get_user(user_id: int, db: Session):
    user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    return user


def get_users(db: Session) -> list[UserSchema]:
    users = db.query(models.users.User).all()
    return users
