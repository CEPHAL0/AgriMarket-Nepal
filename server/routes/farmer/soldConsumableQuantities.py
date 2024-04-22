from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.sold_consumable_quantities import SoldConsumableQuantities
from schemas.SoldConsumableQuantities import (
    SoldConsumableQuantity as SoldConsumableQuantitySchema,
    SoldConsumableQuantityCreate as SoldConsumableQuantityCreateSchema,
)
from services.auth import get_current_user_from_token
from config.enums.role import RoleEnum
from services import auth as auth_service
from logger import logger

router = APIRouter(tags=["Sold Consumable Quantities"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[SoldConsumableQuantitySchema])
def get_sold_consumable_quantities(db: Session = Depends(get_db)):
    try:
        db_sold_consumable_quantities = db.query(SoldConsumableQuantities).all()
        return db_sold_consumable_quantities
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to get sold consumable quantities"
        )


@router.get("/{sold_consumable_id}", response_model=SoldConsumableQuantitySchema)
def get_sold_consumable_quantities(
    sold_consumable_id: int, db: Session = Depends(get_db)
):
    try:
        db_sold_consumable_quantity = (
            db.query(SoldConsumableQuantities)
            .filter(SoldConsumableQuantities.id == sold_consumable_id)
            .first()
        )
        return db_sold_consumable_quantity

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to get sold consumable quantities"
        )
