from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.user_surplus_bookings import UserSurplusBookings
from models.consumables import Consumables
from models.users import Users
from schemas.UserSurplusBookings import (
    UserSurplusBooking as UserSurplusBookingSchema,
    UserSurplusBookingCreate as UserSurplusBookingCreateSchema,
)
from logger import logger
from services import auth as auth_service

router = APIRouter(tags=["User Surplus Bookings"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UserSurplusBookingSchema])
def get_user_surplus_bookings(db: Session = Depends(get_db)):
    try:
        user_surplus_bookings = db.query(UserSurplusBookings).all()
        return user_surplus_bookings
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve User Surplus Bookings"
        )


@router.get("/{user_surplus_booking_id}", response_model=UserSurplusBookingSchema)
def get_user_surplus_booking(
    user_surplus_booking_id: int, db: Session = Depends(get_db)
):
    try:
        user_surplus_booking = (
            db.query(UserSurplusBookings)
            .filter(UserSurplusBookings.id == user_surplus_booking_id)
            .first()
        )
        if user_surplus_booking is None:
            raise HTTPException(
                status_code=404, detail="User Surplus Booking not found"
            )
        return user_surplus_booking

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve User Surplus Booking"
        )


@router.post(
    "/create",
    status_code=201,
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def create_user_surplus_booking(
    user_surplus_booking: UserSurplusBookingCreateSchema, db: Session = Depends(get_db)
):
    try:
        consumable = (
            db.query(Consumables)
            .filter(Consumables.id == user_surplus_booking.consumable_id)
            .first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")

        poster = (
            db.query(Users).filter(Users.id == user_surplus_booking.poster_id).first()
        )
        if poster is None:
            raise HTTPException(status_code=404, detail="Poster not found")

        booker = (
            db.query(Users).filter(Users.id == user_surplus_booking.booker_id).first()
        )
        if booker is None:
            raise HTTPException(status_code=404, detail="Booker not found")

        db_user_surplus_booking = UserSurplusBookings(
            consumable_id=user_surplus_booking.consumable_id,
            poster_id=user_surplus_booking.poster_id,
            booker_id=user_surplus_booking.booker_id,
        )
        db.add(db_user_surplus_booking)
        db.commit()
        db.refresh(db_user_surplus_booking)
        return db_user_surplus_booking

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to create User Surplus Booking"
        )


@router.put(
    "/update/{user_surplus_booking_id}",
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def update_user_surplus_booking(
    user_surplus_booking_id: int,
    user_surplus_booking: UserSurplusBookingCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_user_surplus_booking = (
            db.query(UserSurplusBookings)
            .filter(UserSurplusBookings.id == user_surplus_booking_id)
            .first()
        )
        if db_user_surplus_booking is None:
            raise HTTPException(
                status_code=404, detail="User Surplus Booking not found"
            )

        db_user_surplus_booking.consumable_id = user_surplus_booking.consumable_id
        db_user_surplus_booking.user_id = user_surplus_booking.user_id
        db.commit()
        db.refresh(db_user_surplus_booking)
        return db_user_surplus_booking

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to update User Surplus Booking"
        )


@router.delete(
    "/delete/{user_surplus_booking_id}",
    dependencies=[Depends(auth_service.is_user_farmer_or_admin)],
    tags=["admin_or_farmer"],
)
def delete_user_surplus_booking(
    user_surplus_booking_id: int, db: Session = Depends(get_db)
):
    try:
        db_user_surplus_booking = (
            db.query(UserSurplusBookings)
            .filter(UserSurplusBookings.id == user_surplus_booking_id)
            .first()
        )
        if db_user_surplus_booking is None:
            raise HTTPException(
                status_code=404, detail="User Surplus Booking not found"
            )
        db.delete(db_user_surplus_booking)
        db.commit()

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to delete User Surplus Booking"
        )
