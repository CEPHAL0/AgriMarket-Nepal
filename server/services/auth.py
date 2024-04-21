from datetime import timedelta, datetime
from fastapi import Depends, APIRouter, HTTPException, Header, Request
from fastapi.security import OAuth2PasswordBearer
from schemas.Auth import Register, Login
from schemas.Users import UserComplete
from schemas.DataToken import Token, DataToken
from jose import jwt, JWTError
import os
import schemas
from logger import logger
from sqlalchemy.orm import Session
from models.users import Users
from typing import Annotated
from config.database import SessionLocal
from config.enums.role import RoleEnum
from services import auth as auth_service, users as user_service
from schemas.Auth import Login as LoginSchema
from schemas.Auth import Register as RegisterSchema
from fastapi import Response
from config.database import SessionLocal
from passlib.context import CryptContext


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
SECRET_KET = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRES_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(user_id: int):
    to_encode = {"user_id": user_id}
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})
    encoded_jwt = jwt.encode(to_encode, SECRET_KET, ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KET, ALGORITHM)
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        return payload

    except JWTError as jwe:
        logger.error(jwe)
        raise jwe


def get_current_user_from_token(token):
    try:
        db = SessionLocal()
        payload = decode_token(token)

        user_id = payload.get("user_id")

        user = db.query(Users).filter(Users.id == user_id).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    except HTTPException as httpe:
        logger.error(httpe)
        db.close()
        raise httpe

    except Exception as e:
        logger.error(e)
        db.close()
        raise HTTPException(status_code=400, detail="Failed to get user")
    db.close()


async def is_user_admin(request: Request):
    try:
        jwt = request.cookies.get("jwt")
        user: Users = auth_service.get_current_user_from_token(jwt)
        if user.role != RoleEnum.ADMIN:
            raise HTTPException(detail="Forbidden resource", status_code=401)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=401, detail="Forbidden resource")


async def is_user_farmer_or_admin(request: Request):
    try:
        jwt = request.cookies.get("jwt")
        user: Users = auth_service.get_current_user_from_token(jwt)
        if (user.role != RoleEnum.ADMIN) or (user.role != RoleEnum.Farmer):
            raise HTTPException(detail="Forbidden resource", status_code=401)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=401, detail="Forbidden resource")


async def login(login_schema: LoginSchema, response: Response, db: Session):
    try:
        user = user_service.get_user_by_username(login_schema.username, db)

        if not verify_password(login_schema.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid Credentials")

        jwt_token = create_access_token(user.id)
        response.set_cookie(
            key="jwt", value=jwt_token, expires=ACCESS_TOKEN_EXPIRES_MINUTES
        )

        return {"message": "Login Successfull", "access_token": jwt_token}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe


async def register(register_schema: RegisterSchema, response: Response, db: Session):
    try:
        user = user_service.get_user_by_username(register_schema.username, db)
        if user is not None:
            raise HTTPException(status_code=400, detail="Username already exists")

        user = user_service.get_user_by_email(register_schema.email, db)
        if user is not None:
            raise HTTPException(status_code=400, detail="Email already exists")

        user = user_service.get_user_by_phone_number(register_schema.phone, db)
        if user is not None:
            raise HTTPException(status_code=400, detail="Phone number already in use")

        register_schema.password = get_password_hash(register_schema.password)

        user = user_service.create_user(register_schema, db)

        jwt_token = create_access_token(user.id)
        response.set_cookie(
            key="jwt", value=jwt_token, expires=ACCESS_TOKEN_EXPIRES_MINUTES
        )

        return {"message": "User Created Successfully", "access_token": jwt_token}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to register")
