from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import SessionLocal, Base, engine
from routes import consumables, users, provinces, districts, resources, resourceImages, farmerPerformances, consumableListings, consumableMacros, macroTypes, prices, surplusListings, userSurplusBooking

from models import index
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()


# Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(consumables.router, prefix='/consumables')
app.include_router(users.router, prefix='/users')
app.include_router(provinces.router, prefix='/provinces')
app.include_router(districts.router, prefix='/districts')
app.include_router(resources.router, prefix='/resources')
app.include_router(resourceImages.router, prefix='/resourceImages')
app.include_router(farmerPerformances.router, prefix='/farmerPerformances')
app.include_router(consumableListings.router, prefix='/consumableListings')
app.include_router(consumableMacros.router, prefix='/consumableMacros')
app.include_router(macroTypes.router, prefix='/macroTypes')
app.include_router(prices.router, prefix='/prices')
app.include_router(surplusListings.router, prefix='/surplusListings')
app.include_router(userSurplusBooking.router, prefix='/userSurplusBooking')