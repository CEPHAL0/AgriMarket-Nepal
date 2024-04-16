from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumable_listings import ConsumableListing
from models.districts import Districts
from models.users import User
from schemas.ConsumableListings import ConsumableListings as ConsumableListingSchema, ConsumableListingCreate as ConsumableListingCreateSchema
from logger import logger

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ConsumableListingSchema])
def get_consumable_listings(db: Session = Depends(get_db)):
    try:
        consumable_listings = db.query(ConsumableListing).all()
        return consumable_listings
    except Exception as e:
        logger.error(e)
        raise e


@router.get("/{consumable_listing_id}", response_model=ConsumableListingSchema)
def get_one_consumable_listing(consumable_listing_id: int, db: Session = Depends(get_db)):
    try:
        consumable_listing = db.query(ConsumableListing).filter(ConsumableListing.id == consumable_listing_id).first()
        if consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")
        return consumable_listing
    except Exception as e:
        logger.error(e)
        raise e


@router.post("/", response_model=ConsumableListingSchema, status_code=201)
def create_consumable_listing(consumable_listing: ConsumableListingCreateSchema, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == consumable_listing.user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        district = db.query(Districts).filter(Districts.id == consumable_listing.district_id).first()
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        
        db_consumable_listing = ConsumableListing(consumable_id=consumable_listing.consumable_id, user_id=consumable_listing.user_id, price=consumable_listing.price, district_id=consumable_listing.district_id)
        db.add(db_consumable_listing)
        db.commit()
        db.refresh(db_consumable_listing)
        return db_consumable_listing
    except Exception as e:
        logger.error(e)
        raise e


@router.put("/{consumable_listing_id}", response_model=ConsumableListingSchema)
def update_consumable_listing(consumable_listing_id: int, consumable_listing: ConsumableListingCreateSchema, db: Session = Depends(get_db)):
    try:
        db_consumable_listing = db.query(ConsumableListing).filter(ConsumableListing.id == consumable_listing_id).first()
        if db_consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")
        
        db_consumable_listing.consumable_id = consumable_listing.consumable_id
        db_consumable_listing.user_id = consumable_listing.user_id
        db_consumable_listing.price = consumable_listing.price
        db_consumable_listing.district_id = consumable_listing.district_id
        db.commit()
        db.refresh(db_consumable_listing)
        return db_consumable_listing
    except Exception as e:
        logger.error(e)
        raise e


@router.delete("/{consumable_listing_id}", status_code=204)
def delete_consumable_listing(consumable_listing_id: int, db: Session = Depends(get_db)):
    try:
        consumable_listing = db.query(ConsumableListing).filter(ConsumableListing.id == consumable_listing_id).first()
        if consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")
        
        db.delete(consumable_listing)
        db.commit()
    except Exception as e:
        logger.error(e)
        raise e