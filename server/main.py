from fastapi import FastAPI, Request, HTTPException, Response, status, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config.database import SessionLocal, Base, engine
from fastapi.staticfiles import StaticFiles

from routes.auth import auth
from routes.index import (
    users,
    consumables,
    provinces,
    districts,
    resources,
    resourceImages,
    farmerPerformances,
    consumableListings,
    consumableMacros,
    macroTypes,
    surplusListings,
    prices,
    userSurplusBooking,
)


from services.auth import get_current_user_from_token
from sqlalchemy.orm import Session

from models import index
import sys
import os
from logger import logger

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


PUBLIC_ROUTES_PREFIX = ["/login", "/register", "/docs", "/openapi", "/public", "/images"]


@app.middleware("authorization")
async def is_authorized(request: Request, call_next):
    try:
        if (any(request.url.path.startswith(prefix) for prefix in PUBLIC_ROUTES_PREFIX)):
            return await call_next(request)
        jwt = request.cookies.get("jwt")
        if jwt is None:
            raise HTTPException(status_code=401, detail="Unauthorized")

        user = get_current_user_from_token(jwt)

        response = await call_next(request)
        return response
    
    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Unauthorized"},
        )


app.mount("/images", StaticFiles(directory="public/images"), name="images")

app.include_router(consumables.router, prefix="/consumables")
app.include_router(users.router, prefix="/users")
app.include_router(provinces.router, prefix="/provinces")
app.include_router(districts.router, prefix="/districts")
app.include_router(resources.router, prefix="/resources")
app.include_router(resourceImages.router, prefix="/resourceImages")
app.include_router(farmerPerformances.router, prefix="/farmerPerformances")
app.include_router(consumableListings.router, prefix="/consumableListings")
app.include_router(consumableMacros.router, prefix="/consumableMacros")
app.include_router(macroTypes.router, prefix="/macroTypes")
app.include_router(prices.router, prefix="/prices")
app.include_router(surplusListings.router, prefix="/surplusListings")
app.include_router(userSurplusBooking.router, prefix="/userSurplusBooking")
app.include_router(auth.router)
