from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.resource_images import ResourceImages
from models.resources import Resources
from schemas.ResourceImages import (
    ResourceImage as ResourceImageSchema,
    ResourceImageCreate as ResourceImageCreateSchema,
)
from logger import logger

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ResourceImageSchema])
def get_resource_images(db: Session = Depends(get_db)):
    try:
        resource_images = db.query(ResourceImages).all()
        return resource_images
    except Exception as e:
        logger.error(e)
        raise e


@router.get("/{resource_image_id}", response_model=ResourceImageSchema)
def get_single_resource_image(resource_image_id: int, db: Session = Depends(get_db)):
    try:
        resource_image = (
            db.query(ResourceImages)
            .filter(ResourceImages.id == resource_image_id)
            .first()
        )
        if resource_image is None:
            raise HTTPException(status_code=404, detail="Resource Image not found")
        return resource_image
    except Exception as e:
        logger.error(e)
        raise e


@router.post("/", response_model=ResourceImageSchema, status_code=201)
def create_new_resource_image(
    resource_image: ResourceImageCreateSchema, db: Session = Depends(get_db)
):
    try:
        resource = (
            db.query(Resources)
            .filter(Resources.id == resource_image.resource_id)
            .first()
        )
        if resource is None:
            raise HTTPException(status_code=404, detail="Resource not found")

        db_resource_image = ResourceImages(
            resource_id=resource_image.resource_id,
            image_path=resource_image.image_path,
            order=resource_image.order,
        )
        db.add(db_resource_image)
        db.commit()
        db.refresh(db_resource_image)
        return db_resource_image
    except Exception as e:
        logger.error(e)
        raise e


@router.put("/{resource_image_id}", response_model=ResourceImageSchema)
def update_resource_image(
    resource_image_id: int,
    resource_image: ResourceImageCreateSchema,
    db: Session = Depends(get_db),
):
    try:
        db_resource_image = (
            db.query(ResourceImages)
            .filter(ResourceImages.id == resource_image_id)
            .first()
        )
        if db_resource_image is None:
            raise HTTPException(status_code=404, detail="Resource Image not found")

        db_resource_image.resource_id = resource_image.resource_id
        db_resource_image.image_path = resource_image.image_path
        db_resource_image.order = resource_image.order
        db.commit()
        db.refresh(db_resource_image)
        return db_resource_image
    except Exception as e:
        logger.error(e)
        raise e


@router.delete("/{resource_image_id}", status_code=204)
def delete_resource_image(resource_image_id: int, db: Session = Depends(get_db)):
    try:
        db_resource_image = (
            db.query(ResourceImages)
            .filter(ResourceImages.id == resource_image_id)
            .first()
        )
        if db_resource_image is None:
            raise HTTPException(status_code=404, detail="Resource Image not found")

        db.delete(db_resource_image)
        db.commit()
    except Exception as e:
        logger.error(e)
        raise e
