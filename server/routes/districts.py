from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.districts import Districts
from models.provinces import Provinces
from schemas.Districts import (
    District as DistrictsSchema,
    DistrictCreate as DistrictCreateSchema,
)
from logger import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[DistrictsSchema])
def get_districts(db: Session = Depends(get_db)):
    try:
        districts = db.query(Districts).all()
        return districts
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Districts")


@router.get("/{district_id}", response_model=DistrictsSchema)
def get_district(district_id: int, db: Session = Depends(get_db)):
    try:
        district = db.query(Districts).filter(Districts.id == district_id).first()
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        return district

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve District")


@router.post("/create", response_model=DistrictsSchema, status_code=201)
def create_district(district: DistrictCreateSchema, db: Session = Depends(get_db)):
    try:
        province = (
            db.query(Provinces).filter(Provinces.id == district.province_id).first()
        )
        if province is None:
            raise HTTPException(status_code=404, detail="Province not found")

        db_district = Districts(
            name=district.name,
            province_id=district.province_id,
            ecological_region=district.ecological_region,
        )
        db.add(db_district)
        db.commit()
        db.refresh(db_district)
        return db_district

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise e


@router.put("/update/{district_id}", response_model=DistrictsSchema)
def update_district(
    district_id: int, district: DistrictCreateSchema, db: Session = Depends(get_db)
):
    try:
        db_district = db.query(Districts).filter(Districts.id == district_id).first()
        if db_district is None:
            raise HTTPException(status_code=404, detail="District not found")

        province = (
            db.query(Provinces).filter(Provinces.id == district.province_id).first()
        )
        if province is None:
            raise HTTPException(status_code=404, detail="Province not found")

        db_district.name = district.name
        db_district.province_id = district.province_id
        db.commit()
        db.refresh(db_district)
        return db_district

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise e


@router.delete("/delete/{district_id}")
def delete_district(district_id: int, db: Session = Depends(get_db)):
    try:
        db_district = db.query(Districts).filter(Districts.id == district_id).first()
        if db_district is None:
            raise HTTPException(status_code=404, detail="District not found")

        db.delete(db_district)
        db.commit()
        return {"message": "District deleted successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise e
