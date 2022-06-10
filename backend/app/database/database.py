from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

databaseName = "venture"
dbUser = os.getenv('DATABASE_USERNAME')
dbPass = os.getenv('DATABASE_PASSWORD')
dbHost = "localhost"
DATABASE_URL = f'postgresql+psycopg2://{dbUser}:{dbPass}@{dbHost}/{databaseName}'

engine = create_engine(DATABASE_URL)
engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ORM models are inherited from this class
Base = declarative_base()
