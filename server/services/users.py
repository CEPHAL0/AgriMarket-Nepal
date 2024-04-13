from sqlalchemy.orm import Session

from models import index as models
from schemas import index


def get_user(db: Session, user_id: int):
    return db.query(models.users.User).filter(models.users.User.id == user_id).first()
    
