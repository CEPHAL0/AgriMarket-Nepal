from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.macro_types import MacroTypes
from schemas.MacroTypes import (
    MacroType as MacroTypesSchema,
    MacroTypeCreate as MacroTypesCreateSchema,
)
from logger import logger

router = APIRouter()


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
        raise e


@router.get("/{macro_type_id}", response_model=MacroTypesSchema)
def get_macro_type(macro_type_id: int, db: Session = Depends(get_db)):
    try:
        macro_type = db.query(MacroTypes).filter(MacroTypes.id == macro_type_id).first()
        if macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")
        return macro_type
    except Exception as e:
        logger.error(e)
        raise e


@router.post("/", response_model=MacroTypesSchema, status_code=201)
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
        raise e


@router.put("/{macro_type_id}", response_model=MacroTypesSchema)
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
    except Exception as e:
        logger.error(e)
        raise e


@router.delete("/{macro_type_id}", status_code=204)
def delete_macro_type(macro_type_id: int, db: Session = Depends(get_db)):
    try:
        db_macro_type = (
            db.query(MacroTypes).filter(MacroTypes.id == macro_type_id).first()
        )
        if db_macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")

        db.delete(db_macro_type)
        db.commit()
        return None
    except Exception as e:
        logger.error(e)
        raise e
