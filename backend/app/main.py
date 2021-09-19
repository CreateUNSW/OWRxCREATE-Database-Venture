from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine

from . import models

# uncomment below to create all tables in the postgres database
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()  # run from backend directory: `uvicorn app.main:app --reload`

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.Tag).first()  # Write your query here
