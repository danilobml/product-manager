import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

# create the engine
engine = create_engine(DEV_DATABASE_URL)

# create a section
SessionLocal = sessionmaker(
    # only commit manually
    autocommit=False,
    # update all operations within a transaction to ensure up to date tables before commit:
    autoflsuh=True,
    # binds session to the engine - used for only 1 database
    bind=True
    )

Base = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
