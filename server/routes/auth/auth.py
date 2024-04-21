from fastapi import APIRouter, HTTPException, Depends, Response
from services.auth import (
    create_access_token,
    decode_token,
    get_current_user_from_token,
)
from logger import logger
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from schemas.Auth import Login as LoginSchema, Register as RegisterSchema
from services import users as user_service, auth as auth_service


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/login")
async def login(
    login_schema: LoginSchema, response: Response, db: Session = Depends(get_db)
):
    try:
        response = await auth_service.login(login_schema, response, db)
        return response

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=401, detail="Failed to login")


@router.post("/register")
async def register(
    register_schema: RegisterSchema, response: Response, db: Session = Depends(get_db)
):
    try:
        response = await auth_service.register(register_schema, response, db)
        return response

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=401, detail="Failed to register")
