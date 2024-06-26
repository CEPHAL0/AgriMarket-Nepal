from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
