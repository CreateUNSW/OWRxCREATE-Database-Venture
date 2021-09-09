from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

dbUser = os.getenv('DATABASE_USERNAME')
dbPass = os.getenv('DATABASE_PASSWORD')

DATABASE_URL = f'postgresql://{dbUser}:{dbPass}@postgresserver/db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM models are inherited from this class
Base = declarative_base()
