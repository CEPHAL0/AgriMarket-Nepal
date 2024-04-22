from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.resource_images import ResourceImages
from models.resources import Resources
from schemas.ResourceImages import (
    ResourceImage as ResourceImageSchema,
    ResourceImageCreate as ResourceImageCreateSchema,
)
from logger import logger
from datetime import datetime

router = APIRouter(tags=["Resource Images"])

IMAGE_DIR = "public/images/resource_images"


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
        raise HTTPException(
            status_code=400, detail="Failed to retrieve Resource Images"
        )


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

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Resource Image")


@router.get("/resource/{resource_id}", response_model=list[ResourceImageSchema])
def get_resource_image_by_resource_id(resource_id: int, db: Session = Depends(get_db)):
    try:
        resource_image = (
            db.query(ResourceImages)
            .filter(ResourceImages.resource_id == resource_id)
            .all()
        )
        if resource_image is None:
            raise HTTPException(status_code=404, detail="Resource Image not found")
        return resource_image

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve Resource Image")


@router.post("/create", response_model=ResourceImageSchema, status_code=201)
def create_new_resource_image(
    # resource_image: ResourceImageCreateSchema, 
    resource_id: int = Form(...),
    image_path: UploadFile = File(...),
    order: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        resource = (
            db.query(Resources)
            .filter(Resources.id == resource_id)
            .first()
        )
        if resource is None:
            raise HTTPException(status_code=404, detail="Resource not found")
        
        image_name = "images/resource_images/default.png"
        if image_path is not None:
            formatted_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
            filename = f"{formatted_datetime}-{image_path.filename}"
            image_name = f"images/resource_images/{filename}"
            with open(f"{IMAGE_DIR}/{filename}", "wb") as buffer:
                buffer.write(image_path.file.read())

        db_resource_image = ResourceImages(
            resource_id=resource_id,
            image_path=image_name,
            order=order,
        )
        db.add(db_resource_image)
        db.commit()
        db.refresh(db_resource_image)
        return db_resource_image

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create Resource Image")


@router.put("/update/{resource_image_id}", response_model=ResourceImageSchema)
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

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to update Resource Image")


@router.delete("/delete/{resource_image_id}", status_code=204)
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

    except HTTPException as httpe:
        logger.error(httpe)
        raise httpe

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete Resource Image")
