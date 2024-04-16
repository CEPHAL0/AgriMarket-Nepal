# replace with auth routes






from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.users import User
from schemas.User import User as UserSchema, UserCreate as UserCreateSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserSchema, status_code=201)
def create_new_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    email_exists = db.query(User).filter(User.email == user.email).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    username_exists = db.query(User).filter(User.username == user.username).first()
    if username_exists:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    db_user = User(name=user.name, username=user.username, email=user.email, image=user.image, role=user.role, address=user.address, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user