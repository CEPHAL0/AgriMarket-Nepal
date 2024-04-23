from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumable_listings import ConsumableListings
from models.districts import Districts
from models.consumables import Consumables
from models.users import Users
from schemas.ConsumableListings import (
    ConsumableListing as ConsumableListingSchema,
    ConsumableListingCreate as ConsumableListingCreateSchema,
    ConsumableListingEdit as ConsumableListingEditSchema,
)

from schemas.Quantities import Quantity

from logger import logger
from datetime import datetime


from services.auth import get_current_user_from_token
from config.enums.role import RoleEnum
from services import auth as auth_service

from models.sold_consumable_quantities import SoldConsumableQuantities

from services.auth import get_current_user_from_token

router = APIRouter(tags=["Consumable Listings"])


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


@router.post(
    "/create",
    response_model=ConsumableListingSchema,
    status_code=201,
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def create_consumable_listing(
    request: Request,
    consumable_listing: ConsumableListingCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        user = auth_service.get_current_user_from_token(request.cookies.get("jwt"))

        district = (
            db.query(Districts)
            .filter(Districts.id == consumable_listing.district_id)
            .first()
        )
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        
        consumable = db.query(Consumables).filter(Consumables.id == consumable_listing.consumable_id).first()
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        db_consumable_listing = ConsumableListings(
            consumable_id=consumable_listing.consumable_id,
            user_id=user.id,
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


@router.put(
    "/update/{consumable_listing_id}",
    response_model=ConsumableListingSchema,
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def update_consumable_listing(
    consumable_listing_id: int,
    request: Request,
    consumable_listing: ConsumableListingEditSchema,
    db: Session = Depends(get_db),
):
    try:
        user = auth_service.get_current_user_from_token(request.cookies.get("jwt"))

        db_consumable_listing = (
            db.query(ConsumableListings)
            .filter(
                (ConsumableListings.id == consumable_listing_id),
                (ConsumableListings.user_id == user.id),
            )
            .first()
        )

        if db_consumable_listing is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")

        db_consumable_listing.consumable_id = consumable_listing.consumable_id
        db_consumable_listing.user_id = user.id
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


@router.delete(
    "/delete/{consumable_listing_id}",
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def delete_consumable_listing(
    request: Request, consumable_listing_id: int, db: Session = Depends(get_db)
):
    try:
        user = auth_service.get_current_user_from_token(request.cookies.get("jwt"))
        consumable_listing = (
            db.query(ConsumableListings)
            .filter(
                (ConsumableListings.id == consumable_listing_id),
                (ConsumableListings.user_id == user.id),
            )
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


@router.patch(
    "/reduce/{consumable_listing_id}",
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def reduce_quantity(
    request: Request,
    quantity_to_reduce: Quantity,
    consumable_listing_id: int,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("jwt")
        user: Users = get_current_user_from_token(token)

        db_consumable: ConsumableListings = (
            db.query(ConsumableListings)
            .filter(
                (ConsumableListings.id == consumable_listing_id),
                (ConsumableListings.user_id == user.id),
            )
            .first()
        )

        if db_consumable is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")

        if quantity_to_reduce.quantity is None:
            raise HTTPException(
                status_code=400, detail="Quantity to reduce not provided"
            )
        elif quantity_to_reduce.quantity > db_consumable.quantity:
            raise HTTPException(
                status_code=400,
                detail="Quantity cannot exceed max quantity of listing",
            )

        db_consumable.quantity = db_consumable.quantity - quantity_to_reduce.quantity

        db_sold_consumable_quantity: SoldConsumableQuantities = (
            SoldConsumableQuantities(
                consumable_id=db_consumable.id,
                farmer_id=user.id,
                quantity_sold=quantity_to_reduce.quantity,
                date_sold=datetime.now(),
            )
        )

        db.add(db_sold_consumable_quantity)

        db.commit()
        db.refresh(db_consumable)
        return {"message": "Quantity Reduced Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to reduce quantity")


@router.patch(
    "/add/{consumable_listing_id}",
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def add_quantity(
    request: Request,
    quantity_to_add: Quantity,
    consumable_listing_id: int,
    db: Session = Depends(get_db),
):

    try:
        token = request.cookies.get("jwt")
        user: Users = get_current_user_from_token(token)

        db_consumable: ConsumableListings = (
            db.query(ConsumableListings)
            .filter(
                (ConsumableListings.id == consumable_listing_id),
                (ConsumableListings.user_id == user.id),
            )
            .first()
        )

        if db_consumable is None:
            raise HTTPException(status_code=404, detail="Consumable Listing not found")

        if quantity_to_add.quantity is None:
            raise HTTPException(status_code=400, detail="Quantity to add not provided")

        db_consumable.quantity = db_consumable.quantity + quantity_to_add.quantity

        db.commit()
        db.refresh(db_consumable)
        return {"message": "Quantity Added Successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to reduce quantity")
