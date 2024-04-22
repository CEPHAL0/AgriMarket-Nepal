from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.surplus_listings import SurplusListings
from models.consumables import Consumables
from schemas.SurplusListings import (
    SurplusListing as SurplusListingsSchema,
    SurplusListingCreate as SurplusListingCreateSchema,
)
from logger import logger
from models.users import Users
from services.auth import get_current_user_from_token

router = APIRouter(tags=["Surplus Listings"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[SurplusListingsSchema])
def get_surplus_listings(db: Session = Depends(get_db)):
    try:
        surplus_listings = db.query(SurplusListings).all()
        return surplus_listings
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Surplus Listings"
        )


@router.get("/{surplus_listing_id}", response_model=SurplusListingsSchema)
def get_surplus_listing(surplus_listing_id: int, db: Session = Depends(get_db)):
    try:
        surplus_listing = (
            db.query(SurplusListings)
            .filter(SurplusListings.id == surplus_listing_id)
            .first()
        )
        if surplus_listing is None:
            raise HTTPException(status_code=404, detail="Surplus Listing not found")
        return surplus_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Surplus Listing"
        )


@router.post("/create", response_model=SurplusListingsSchema, status_code=201)
def create_surplus_listing(
    surplus_listing: SurplusListingCreateSchema, db: Session = Depends(get_db)
):
    try:
        consumable = (
            db.query(Consumables)
            .filter(Consumables.id == surplus_listing.consumable_id)
            .first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        db_surplus_listing = SurplusListings(
            consumable_id=surplus_listing.consumable_id,
            price=surplus_listing.price,
            farmer_id=surplus_listing.farmer_id,
        )
        db.add(db_surplus_listing)
        db.commit()
        db.refresh(db_surplus_listing)
        return db_surplus_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Surplus Listing")


@router.put("/update/{surplus_listing_id}", response_model=SurplusListingsSchema)
def update_surplus_listing(
    surplus_listing_id: int,
    request: Request,
    surplus_listing: SurplusListingCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("jwt")
        user: Users = get_current_user_from_token(token)

        db_surplus_listing: SurplusListings = (
            db.query(SurplusListings)
            .filter(SurplusListings.id == surplus_listing_id)
            .first()
        )
        if db_surplus_listing is None:
            raise HTTPException(status_code=404, detail="Surplus Listing not found")

        if db_surplus_listing.farmer_id != user.id:
            raise HTTPException(status_code=404, detail="Surplus Listing not found")

        db_surplus_listing.consumable_id = surplus_listing.consumable_id
        db_surplus_listing.farmer_id = surplus_listing.farmer_id
        db_surplus_listing.price = surplus_listing.price

        if surplus_listing.booked is not None:
            db_surplus_listing.booked = surplus_listing.booked

        db.commit()
        db.refresh(db_surplus_listing)
        return db_surplus_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Surplus Listing")


@router.delete("/delete/{surplus_listing_id}")
def delete_surplus_listing(surplus_listing_id: int, db: Session = Depends(get_db)):
    try:
        db_surplus_listing = (
            db.query(SurplusListings)
            .filter(SurplusListings.id == surplus_listing_id)
            .first()
        )
        if db_surplus_listing is None:
            raise HTTPException(status_code=404, detail="Surplus Listing not found")
        db.delete(db_surplus_listing)
        db.commit()
        return {"message": "Successfully deleted Surplus Listing"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Surplus Listing")
