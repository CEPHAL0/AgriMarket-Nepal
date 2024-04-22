from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumable_macros import ConsumableMacros
from models.consumables import Consumables
from models.macro_types import MacroTypes
from schemas.ConsumableMacros import (
    ConsumableMacro as ConsumableMacrosSchema,
    ConsumableMacroCreate as ConsumableMacrosCreateSchema,
)
from logger import logger
from services import auth as auth_service

router = APIRouter(tags=["Consumable Macros"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ConsumableMacrosSchema])
def get_consumable_macros(db: Session = Depends(get_db)):
    try:
        consumable_macros = db.query(ConsumableMacros).all()
        return consumable_macros

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Consumable Macros"
        )


@router.get("/{consumable_macro_id}", response_model=ConsumableMacrosSchema)
def get_one_consumable_macro(consumable_macro_id: int, db: Session = Depends(get_db)):
    try:
        consumable_macro = (
            db.query(ConsumableMacros)
            .filter(ConsumableMacros.id == consumable_macro_id)
            .first()
        )
        if consumable_macro is None:
            raise HTTPException(status_code=404, detail="ConsumableMacro not found")
        return consumable_macro

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Consumable Macro"
        )


@router.post(
    "/create",
    response_model=ConsumableMacrosSchema,
    status_code=201,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def create_consumable_macro(
    consumable_macro: ConsumableMacrosCreateSchema, db: Session = Depends(get_db)
):
    try:
        consumable = (
            db.query(Consumables)
            .filter(Consumables.id == consumable_macro.consumable_id)
            .first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        macro_type = (
            db.query(MacroTypes)
            .filter(MacroTypes.id == consumable_macro.macro_type_id)
            .first()
        )
        if macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")

        db_consumable_macro = ConsumableMacros(
            consumable_id=consumable_macro.consumable_id,
            macro_type_id=consumable_macro.macro_type_id,
            quantity=consumable_macro.quantity,
        )
        db.add(db_consumable_macro)
        db.commit()
        db.refresh(db_consumable_macro)
        return db_consumable_macro

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Consumable Macro")


@router.put(
    "/update/{consumable_macro_id}",
    response_model=ConsumableMacrosSchema,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def update_consumable_macro(
    consumable_macro_id: int,
    consumable_macro: ConsumableMacrosCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_consumable_macro = (
            db.query(ConsumableMacros)
            .filter(ConsumableMacros.id == consumable_macro_id)
            .first()
        )
        if db_consumable_macro is None:
            raise HTTPException(status_code=404, detail="ConsumableMacro not found")

        consumable = (
            db.query(Consumables)
            .filter(Consumables.id == consumable_macro.consumable_id)
            .first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        macro_type = (
            db.query(MacroTypes)
            .filter(MacroTypes.id == consumable_macro.macro_type_id)
            .first()
        )
        if macro_type is None:
            raise HTTPException(status_code=404, detail="MacroType not found")

        db_consumable_macro.consumable_id = consumable_macro.consumable_id
        db_consumable_macro.macro_type_id = consumable_macro.macro_type_id
        db_consumable_macro.quantity = consumable_macro.quantity
        db.commit()
        db.refresh(db_consumable_macro)
        return db_consumable_macro

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Consumable Macro")


@router.delete(
    "/delete/{consumable_macro_id}",
    status_code=204,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def delete_consumable_macro(consumable_macro_id: int, db: Session = Depends(get_db)):
    try:
        db_consumable_macro = (
            db.query(ConsumableMacros)
            .filter(ConsumableMacros.id == consumable_macro_id)
            .first()
        )
        if db_consumable_macro is None:
            raise HTTPException(status_code=404, detail="Consumable Macro not found")

        db.delete(db_consumable_macro)
        db.commit()
        return {"message": "Deleted Consumable Macro Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Consumable Macro")
