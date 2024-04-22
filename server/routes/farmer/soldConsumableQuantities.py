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


@router.get(
    "/{sold_consumable_quantity_id}", response_model=SoldConsumableQuantitySchema
)
def get_sold_consumable_quantities(
    sold_consumable_quantity_id: int, db: Session = Depends(get_db)
):
    try:
        db_sold_consumable_quantity = (
            db.query(SoldConsumableQuantities)
            .filter(SoldConsumableQuantities.id == sold_consumable_quantity_id)
            .first()
        )

        if db_sold_consumable_quantity is None:
            raise HTTPException(
                status_code=404, detail="Sold Consumable Listing not found"
            )

        return db_sold_consumable_quantity

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to get sold consumable quantities"
        )


@router.put(
    "/{sold_consumable_quantity_id}",
    response_model=SoldConsumableQuantitySchema,
    dependencies=[Depends(auth_service.is_user_admin)],
)
def update_sold_consumable_quantity(
    sold_consumable_quantity_id: int,
    sold_consumable_quantity: SoldConsumableQuantityCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_sold_consumable_quantity: SoldConsumableQuantities = (
            db.query(SoldConsumableQuantities)
            .filter(SoldConsumableQuantities.id == sold_consumable_quantity_id)
            .first()
        )

        if db_sold_consumable_quantity is None:
            raise HTTPException(
                status_code=404, detail="Sold Consumable Listing not found"
            )

        db_sold_consumable_quantity.consumable_id = (
            sold_consumable_quantity.consumable_id
        )

        db_sold_consumable_quantity.farmer_id = sold_consumable_quantity.farmer_id

        db_sold_consumable_quantity.quantity_sold = (
            sold_consumable_quantity.quantity_sold
        )

        db_sold_consumable_quantity.date_sold = sold_consumable_quantity.date_sold

        db.commit()
        db.refresh(db_sold_consumable_quantity)
        return db_sold_consumable_quantity

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to update Sold Consumable Quantity"
        )


@router.delete(
    "/{sold_consumable_quantity_id}", dependencies=[Depends(auth_service.is_user_admin)]
)
def delete_sold_consumable_quantity_id(
    sold_consumable_quantity_id: int, db: Session = Depends(get_db)
):
    try:
        db_sold_consumable_quantity = (
            db.query(SoldConsumableQuantities)
            .filter(SoldConsumableQuantities.id == sold_consumable_quantity_id)
            .first()
        )

        if db_sold_consumable_quantity is None:
            raise HTTPException(
                status_code=404, detail="Sold Consumable Listing not found"
            )

        db.delete(db_sold_consumable_quantity)
        db.commit()
        return {"message": "Sold Consumable Quantity Deleted Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to delete Sold Consumable Quantity"
        )
