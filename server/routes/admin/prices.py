from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.prices import Prices
from models.consumables import Consumables
from schemas.Prices import Price as PricesSchema, PriceCreate as PricesCreateSchema
from logger import logger
from services import auth as auth_service
from datetime import datetime
from typing import List

router = APIRouter(tags=["Prices"])


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
def get_price_by_id(price_id: int, db: Session = Depends(get_db)):
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
    

@router.get("/consumable/{consumable_id}", response_model=list[PricesSchema])
def get_price_by_consumable_id(consumable_id: int, db: Session = Depends(get_db)):
    try:
        consumables = db.query(Consumables).filter(Consumables.id == consumable_id).all()
        if consumables is None:
            raise HTTPException(status_code=404, detail="Consumable not found")
        
        prices = db.query(Prices).filter(Prices.consumable_id == consumable_id).all()
        if prices is None:
            raise HTTPException(status_code=404, detail="Price not found")
        return prices

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Price for provided Consumable")


@router.get("/consumable/today/{consumable_id}", response_model=PricesSchema)
def get_price_by_consumable_today(consumable_id: int, db: Session = Depends(get_db)):
    try:
        consumable = db.query(Consumables).filter(Consumables.id == consumable_id).first()
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")
        price = db.query(Prices).filter(Prices.consumable_id == consumable_id).all()

        filtered_data = []
        for item in price:
            item_date = datetime.strptime(str(item.date), "%Y-%m-%d %H:%M:%S").date()
            if item_date == datetime.now().date():
                filtered_data.append(item)
        
        print('filtered data: ', filtered_data[0])
        print(len(filtered_data))

        if len(filtered_data) == 0:
            raise HTTPException(status_code=404, detail="Price for today found")
        
        return filtered_data[0]

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Price for provided Consumable")


@router.post(
    "/create",
    response_model=PricesSchema,
    status_code=201,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def create_price(price: PricesCreateSchema, db: Session = Depends(get_db)):
    try:
        consumable = (
            db.query(Consumables).filter(Consumables.id == price.consumable_id).first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        db_price = Prices(
            consumable_id=price.consumable_id, price=price.price, date=price.date
        )
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


@router.put(
    "/update/{price_id}",
    response_model=PricesSchema,
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
def update_price(
    price_id: int, price: PricesCreateSchema, db: Session = Depends(get_db)
):
    try:
        db_price = db.query(Prices).filter(Prices.id == price_id).first()
        if db_price is None:
            raise HTTPException(status_code=404, detail="Price not found")
        db_price.price = price.price
        db_price.date = price.date
        db.commit()
        return db_price

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Price")


@router.delete(
    "/delete/{price_id}",
    dependencies=[Depends(auth_service.is_user_admin)],
    tags=["admin"],
)
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
