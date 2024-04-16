from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.resources import Resources
from models.users import User
from schemas.Resources import Resources as ResourcesSchema, ResourceCreate as ResourcesCreateSchema
from logger import logger

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ResourcesSchema])
def get_resources(db: Session = Depends(get_db)):
    try:
        resources = db.query(Resources).all()
        return resources
    except Exception as e:
        logger.error(e)
        raise e


@router.get("/{resource_id}", response_model=ResourcesSchema)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    try:
        resource = db.query(Resources).filter(Resources.id == resource_id).first()
        if resource is None:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource
    except Exception as e:
        logger.error(e)
        raise e


@router.post("/", response_model=ResourcesSchema, status_code=201)
def create_resource(resource: ResourcesCreateSchema, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == resource.author_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db_resource = Resources(audience=resource.audience, title=resource.title, description=resource.description, author_id=resource.author_id)
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
        return db_resource
    except Exception as e:
        logger.error(e)
        raise e


@router.put("/{resource_id}", response_model=ResourcesSchema)
def update_resource(resource_id: int, resource: ResourcesCreateSchema, db: Session = Depends(get_db)):
    try:
        db_resource = db.query(Resources).filter(Resources.id == resource_id).first()
        if resource is None:
            raise HTTPException(status_code=404, detail="Resource not found")
        
        user = db.query(User).filter(User.id == resource.author_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db_resource.audience
        return resource
    except Exception as e:
        logger.error(e)
        raise e


@router.delete("/{resource_id}", status_code=204)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    try:
        db_resource = db.query(Resources).filter(Resources.id == resource_id).first()
        if db_resource is None:
            raise HTTPException(status_code=404, detail="Resource not found")
        
        db.delete(db_resource)
        db.commit()
        return
    except Exception as e:
        logger.error(e)
        raise e