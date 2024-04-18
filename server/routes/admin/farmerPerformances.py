from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.farmer_performances import FarmerPerformances
from models.users import Users
from schemas.FarmerPerformances import (
    FarmerPerformance as FarmerPerformanceSchema,
    FarmerPerformanceCreate as FarmerPerformanceCreateSchema,
)
from logger import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[FarmerPerformanceSchema])
def get_farmer_performances(db: Session = Depends(get_db)):
    try:
        farmer_performances = db.query(FarmerPerformances).all()
        return farmer_performances

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Farmer Performances"
        )


@router.get("/{farmer_performance_id}", response_model=FarmerPerformanceSchema)
def get_single_farmer_performance(
    farmer_performance_id: int, db: Session = Depends(get_db)
):
    try:
        farmer_performance = (
            db.query(FarmerPerformances)
            .filter(FarmerPerformances.id == farmer_performance_id)
            .first()
        )
        if farmer_performance is None:
            raise HTTPException(status_code=404, detail="Farmer Performance not found")
        return farmer_performance

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Farmer Performance"
        )


@router.post("/create", response_model=FarmerPerformanceSchema, status_code=201)
def create_new_farmer_performance(
    farmer_performance: FarmerPerformanceCreateSchema, db: Session = Depends(get_db)
):
    try:
        user = db.query(Users).filter(Users.id == farmer_performance.farmer_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Users not found")

        db_farmer_performance = FarmerPerformances(
            farmer_id=farmer_performance.farmer_id,
            performance=farmer_performance.performance,
        )
        db.add(db_farmer_performance)
        db.commit()
        db.refresh(db_farmer_performance)
        return db_farmer_performance

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to create Farmer Performance"
        )


@router.put("/update/{farmer_performance_id}", response_model=FarmerPerformanceSchema)
def update_farmer_performance(
    farmer_performance_id: int,
    farmer_performance: FarmerPerformanceCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_farmer_performance = (
            db.query(FarmerPerformances)
            .filter(FarmerPerformances.id == farmer_performance_id)
            .first()
        )
        if db_farmer_performance is None:
            raise HTTPException(status_code=404, detail="Farmer Performance not found")

        db_farmer_performance.farmer_id = farmer_performance.farmer_id
        db_farmer_performance.performance = farmer_performance.performance
        db.commit()
        db.refresh(db_farmer_performance)
        return db_farmer_performance

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to update Farmer Performance"
        )


@router.delete("/delete/{farmer_performance_id}", status_code=204)
def delete_farmer_performance(
    farmer_performance_id: int, db: Session = Depends(get_db)
):
    try:
        farmer_performance = (
            db.query(FarmerPerformances)
            .filter(FarmerPerformances.id == farmer_performance_id)
            .first()
        )
        if farmer_performance is None:
            raise HTTPException(status_code=404, detail="Farmer Performance not found")

        db.delete(farmer_performance)
        db.commit()
        return {"message": "Deleted Farmer Performance successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to delete Farmer Performances"
        )
