from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.provinces import Provinces
from schemas.Provinces import Provinces as ProvincesSchema, ProvincesCreate as ProvincesCreateSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ProvincesSchema])
def get_provinces(db: Session = Depends(get_db)):
    provinces = db.query(Provinces).all()
    return provinces


@router.get("/{province_id}", response_model=ProvincesSchema)
def get_province_by_id(province_id: int, db: Session = Depends(get_db)):
    province = db.query(Provinces).filter(Provinces.id == province_id).first()
    if province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return province


@router.post("/", response_model=ProvincesSchema, status_code=201)
def create_province(province: ProvincesCreateSchema, db: Session = Depends(get_db)):
    db_province = Provinces(name=province.name)
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province


@router.put("/{province_id}", response_model=ProvincesSchema)
def update_province(province_id: int, province: ProvincesCreateSchema, db: Session = Depends(get_db)):
    db_province = db.query(Provinces).filter(Provinces.id == province_id).first()
    if db_province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    db_province.name = province.name
    db.commit()
    db.refresh(db_province)
    return db_province


@router.delete("/{province_id}")
def delete_province(province_id: int, db: Session = Depends(get_db)):
    db_province = db.query(Provinces).filter(Provinces.id == province_id).first()
    if db_province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    db.delete(db_province)
    db.commit()
    return {"message": "Province deleted successfully"}