import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker

from src.models import *


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

db_url = f"postgresql://{db_user}:{db_password}@postgres/{db_name}"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    SQLModel.metadata.create_all(engine)
