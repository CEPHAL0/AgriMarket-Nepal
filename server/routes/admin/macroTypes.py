from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.macro_types import MacroTypes
from schemas.MacroTypes import (
    MacroType as MacroTypesSchema,
    MacroTypeCreate as MacroTypesCreateSchema,
)
from logger import logger
from services import auth as auth_service

router = APIRouter(tags=["Macro Types"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[MacroTypesSchema])
def get_macro_types(db: Session = Depends(get_db)):
    try:
        macro_types = db.query(MacroTypes).all()
        return macro_types

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Macro Types")


@router.get("/{macro_type_id}", response_model=MacroTypesSchema)
def get_macro_type(macro_type_id: int, db: Session = Depends(get_db)):
    try:
        macro_type = db.query(MacroTypes).filter(MacroTypes.id == macro_type_id).first()
        if macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")
        return macro_type

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Macro Type")


@router.post(
    "/create",
    response_model=MacroTypesSchema,
    status_code=201,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def create_macro_type(
    macro_type: MacroTypesCreateSchema, db: Session = Depends(get_db)
):
    try:
        db_macro_type = MacroTypes(name=macro_type.name)
        db.add(db_macro_type)
        db.commit()
        db.refresh(db_macro_type)
        return db_macro_type

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Macro Types")


@router.put(
    "/update/{macro_type_id}",
    response_model=MacroTypesSchema,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def update_macro_type(
    macro_type_id: int,
    macro_type: MacroTypesCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_macro_type = (
            db.query(MacroTypes).filter(MacroTypes.id == macro_type_id).first()
        )
        if db_macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")

        db_macro_type.name = macro_type.name
        db.commit()
        db.refresh(db_macro_type)
        return db_macro_type

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Macro Type")


@router.delete(
    "/delete/{macro_type_id}",
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def delete_macro_type(macro_type_id: int, db: Session = Depends(get_db)):
    try:
        db_macro_type = (
            db.query(MacroTypes).filter(MacroTypes.id == macro_type_id).first()
        )
        if db_macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")

        db.delete(db_macro_type)
        db.commit()
        return {"message": "Deleted Macro Type Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Macro Type")
