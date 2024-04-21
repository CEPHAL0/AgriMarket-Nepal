from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumable_listings import ConsumableListings
from models.districts import Districts
from models.users import Users
from schemas.ConsumableListings import (
    ConsumableListing as ConsumableListingSchema,
    ConsumableListingCreate as ConsumableListingCreateSchema,
)
from logger import logger
from datetime import datetime


from services.auth import get_current_user_from_token
from config.enums.role import RoleEnum

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
        consumable_listings = db.query(ConsumableListings).all()
        return consumable_listings

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Consumable Listings"
        )


@router.get("/{consumable_listing_id}", response_model=ConsumableListingSchema)
def get_one_consumable_listing(
    consumable_listing_id: int, db: Session = Depends(get_db)
):
    try:
        consumable_listing = (
            db.query(ConsumableListings)
            .filter(ConsumableListings.id == consumable_listing_id)
            .first()
        )
        if consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")
        return consumable_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Consumable Listing"
        )


@router.post("/create", response_model=ConsumableListingSchema, status_code=201)
def create_consumable_listing(
    consumable_listing: ConsumableListingCreateSchema, db: Session = Depends(get_db)
):
    try:
        user = db.query(Users).filter(Users.id == consumable_listing.user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        district = (
            db.query(Districts)
            .filter(Districts.id == consumable_listing.district_id)
            .first()
        )
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")

        db_consumable_listing = ConsumableListings(
            consumable_id=consumable_listing.consumable_id,
            user_id=consumable_listing.user_id,
            price=consumable_listing.price,
            district_id=consumable_listing.district_id,
            quantity=consumable_listing.quantity,
            posted_date=datetime.today(),
            expiry_date=consumable_listing.expiry_date,
        )
        db.add(db_consumable_listing)
        db.commit()
        db.refresh(db_consumable_listing)
        return db_consumable_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to create Consumable Listings"
        )


@router.put("/update/{consumable_listing_id}", response_model=ConsumableListingSchema)
def update_consumable_listing(
    consumable_listing_id: int,
    consumable_listing: ConsumableListingCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_consumable_listing = (
            db.query(ConsumableListings)
            .filter(ConsumableListings.id == consumable_listing_id)
            .first()
        )
        if db_consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")

        db_consumable_listing.consumable_id = consumable_listing.consumable_id
        db_consumable_listing.user_id = consumable_listing.user_id
        db_consumable_listing.price = consumable_listing.price
        db_consumable_listing.district_id = consumable_listing.district_id
        db_consumable_listing.quantity = consumable_listing.quantity
        db_consumable_listing.posted_date = consumable_listing.posted_date
        db.commit()
        db.refresh(db_consumable_listing)
        return db_consumable_listing

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to update Consumable Listing"
        )


@router.delete("/delete/{consumable_listing_id}", status_code=204)
def delete_consumable_listing(
    consumable_listing_id: int, db: Session = Depends(get_db)
):
    try:
        consumable_listing = (
            db.query(ConsumableListings)
            .filter(ConsumableListings.id == consumable_listing_id)
            .first()
        )
        if consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")

        db.delete(consumable_listing)
        db.commit()
        return {"message": "Deleted Consumable Listing Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to delete Consumable Listing"
        )


@router.patch("/reduce/{consumable_listing_id}")
def reduce_quantity(
    request: Request,
    consumable_listing_id: int,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("jwt")
        user: Users = get_current_user_from_token(token)

        if user.role != RoleEnum.ADMIN:
            db_consumable: ConsumableListings = (
                db.query(ConsumableListings)
                .filter(
                    (ConsumableListings.id == consumable_listing_id)
                    & (ConsumableListings.user_id == user.id)
                )
                .first()
            )
            if db_consumable is None:
                raise HTTPException(
                    status_code=404, detail="Consumable Listing not found"
                )
            
            if request.body.get("quantity") is None:
                raise HTTPException(
                    status_code=400, detail="Quantity to reduce not provided"
                )
            elif float(request.body.get("quantity")) > db_consumable.quantity:
                raise HTTPException(
                    status_code=400,
                    detail="Quantity cannot exceed max quantity of listing",
                )
            else:
                db_consumable.quantity = db_consumable.quantity - float(request.body.get("quantity"))
                db.commit()
                db.refresh(db_consumable)

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to reduce quantity")


@router.patch("/add/{consumable_listing_id}")
def reduce_quantity(
    request: Request,
    consumable_listing_id: int,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("jwt")
        user: Users = get_current_user_from_token(token)

        if user.role != RoleEnum.ADMIN:
            db_consumable: ConsumableListings = (
                db.query(ConsumableListings)
                .filter(
                    (ConsumableListings.id == consumable_listing_id)
                    & (ConsumableListings.user_id == user.id)
                )
                .first()
            )
            if db_consumable is None:
                raise HTTPException(
                    status_code=404, detail="Consumable Listing not found"
                )
            
            if request.body.get("quantity") is None:
                raise HTTPException(
                    status_code=400, detail="Quantity to add not provided"
                )
            else:
                db_consumable.quantity = db_consumable.quantity + float(request.body.get("quantity"))
                db.commit()
                db.refresh(db_consumable)

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to add quantity")