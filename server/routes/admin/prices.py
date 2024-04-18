from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.prices import Prices
from models.consumables import Consumables
from schemas.Prices import Price as PricesSchema, PriceCreate as PricesCreateSchema
from logger import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[PricesSchema])
def get_prices(db: Session = Depends(get_db)):
    try:
        prices = db.query(Prices).all()
        return prices
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Prices")


@router.get("/{price_id}", response_model=PricesSchema)
def get_price(price_id: int, db: Session = Depends(get_db)):
    try:
        price = db.query(Prices).filter(Prices.id == price_id).first()
        if price is None:
            raise HTTPException(status_code=404, detail="Price not found")
        return price

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Price")


@router.post("/create", response_model=PricesSchema, status_code=201)
def create_price(price: PricesCreateSchema, db: Session = Depends(get_db)):
    try:
        consumable = (
            db.query(Consumables).filter(Consumables.id == price.consumable_id).first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        db_price = Prices(consumable_id=price.consumable_id, price=price.price)
        db.add(db_price)
        db.commit()
        db.refresh(db_price)
        return db_price

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Prices")


@router.put("/update/{price_id}", response_model=PricesSchema)
def update_price(
    price_id: int, price: PricesCreateSchema, db: Session = Depends(get_db)
):
    try:
        db_price = db.query(Prices).filter(Prices.id == price_id).first()
        if db_price is None:
            raise HTTPException(status_code=404, detail="Price not found")
        db_price.price = price.price
        db.commit()
        return db_price

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Price")


@router.delete("/delete/{price_id}")
def delete_price(price_id: int, db: Session = Depends(get_db)):
    try:
        db_price = db.query(Prices).filter(Prices.id == price_id).first()
        if db_price is None:
            raise HTTPException(status_code=404, detail="Price not found")
        db.delete(db_price)
        db.commit()
        return {"message": "Deleted Price Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Price")
