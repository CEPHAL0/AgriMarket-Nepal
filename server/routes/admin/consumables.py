from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.consumables import Consumables
from schemas.Consumables import (
    Consumable as ConsumablesSchema,
    ConsumableCreate as ConsumablesCreateSchema,
)
from logger import logger
from datetime import datetime

router = APIRouter()

IMAGE_DIR = "public/images/consumables"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ConsumablesSchema])
def get_consumables(db: Session = Depends(get_db)):
    try:
        consumables = db.query(Consumables).all()
        return consumables
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Consumables")


@router.get("/{consumable_id}", response_model=ConsumablesSchema)
def get_consumable(consumable_id: int, db: Session = Depends(get_db)):
    try:
        consumable = (
            db.query(Consumables).filter(Consumables.id == consumable_id).first()
        )
        if consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")
        return consumable

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Consumable")


@router.post("/create", response_model=ConsumablesSchema, status_code=201)
def create_consumable(
    # consumable: ConsumablesCreateSchema, 
    db: Session = Depends(get_db),
    name: str = Form(...),
    type: str = Form(...),
    image_path: UploadFile = File(None)
):
    try:
        image_name = "images/consumables/default.png"
        if image_path is not None:
            formatted_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
            filename = f"{formatted_datetime}-{image_path.filename}"
            image_name = f"images/consumables/{filename}"
            with open(f"{IMAGE_DIR}/{filename}", "wb") as buffer:
                buffer.write(image_path.file.read())

        db_consumable = Consumables(
            name=name, type=type, image_path=image_name
        )
        db.add(db_consumable)
        db.commit()
        db.refresh(db_consumable)
        return db_consumable

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Consumable")


@router.put("/update/{consumable_id}", response_model=ConsumablesSchema)
def update_consumable(
    consumable_id: int,
    consumable: ConsumablesCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_consumable = (
            db.query(Consumables).filter(Consumables.id == consumable_id).first()
        )
        if db_consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")
        setattr(db_consumable, "name", consumable.name)
        setattr(db_consumable, "type", consumable.type)
        db.commit()
        db.refresh(db_consumable)
        return db_consumable

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Consumable")


@router.delete("/delete/{consumable_id}")
def delete_consumable(consumable_id: int, db: Session = Depends(get_db)):
    try:
        db_consumable = (
            db.query(Consumables).filter(Consumables.id == consumable_id).first()
        )
        if db_consumable is None:
            raise HTTPException(status_code=404, detail="Consumable not found")
        db.delete(db_consumable)
        db.commit()
        return {"message": "Consumable deleted successfully"}

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Consumables")
