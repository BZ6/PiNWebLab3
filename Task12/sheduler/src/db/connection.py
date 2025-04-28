from sqlmodel import SQLModel, Session, create_engine

from src.db.models import User, Priority, Task, ScheduleTask, TimeEntry, Schedule, Notification

import os
from dotenv import load_dotenv


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_url = f"postgresql://{db_user}:{db_password}@postgres/{db_name}"

engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
