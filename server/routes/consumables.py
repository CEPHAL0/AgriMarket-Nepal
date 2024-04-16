from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumables import Consumables
from schemas.Consumables import Consumables as ConsumablesSchema, ConsumablesCreate as ConsumablesCreateSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/consumables", response_model=list[ConsumablesSchema])
def get_consumables(db: Session = Depends(get_db)):
    consumables = db.query(Consumables).all()
    return consumables


@router.get("/consumables/{consumable_id}", response_model=ConsumablesSchema)
def get_consumable(consumable_id: int, db: Session = Depends(get_db)):
    consumable = db.query(Consumables).filter(Consumables.id == consumable_id).first()
    if consumable is None:
        raise HTTPException(status_code=404, detail="Consumable not found")
    return consumable


@router.post("/consumables", response_model=ConsumablesSchema, status_code=201)
def create_consumable(consumable: ConsumablesCreateSchema, db: Session = Depends(get_db)):
    db_consumable = Consumables(name=consumable.name, type=consumable.type, image_path=consumable.image_path)
    db.add(db_consumable)
    db.commit()
    db.refresh(db_consumable)
    return db_consumable


@router.put("/consumables/{consumable_id}", response_model=ConsumablesSchema)
def update_consumable(consumable_id: int, consumable: ConsumablesCreateSchema, db: Session = Depends(get_db)):
    db_consumable = db.query(Consumables).filter(Consumables.id == consumable_id).first()
    if db_consumable is None:
        raise HTTPException(status_code=404, detail="Consumable not found")
    db_consumable.name = consumable.name
    db_consumable.type = consumable.type
    db.commit()
    db.refresh(db_consumable)
    return db_consumable


@router.delete("/consumables/{consumable_id}")
def delete_consumable(consumable_id: int, db: Session = Depends(get_db)):
    db_consumable = db.query(Consumables).filter(Consumables.id == consumable_id).first()
    if db_consumable is None:
        raise HTTPException(status_code=404, detail="Consumable not found")
    db.delete(db_consumable)
    db.commit()
    return {"message": "Consumable deleted successfully"}