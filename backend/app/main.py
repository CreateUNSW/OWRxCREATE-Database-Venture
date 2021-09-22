from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal

from models import models

from database.database import get_db, engine

# uncomment below to create all tables in the postgres database
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()  # run from backend directory: `uvicorn app.main:app --reload`
app.include_router(auth.router)

@app.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.Tag).first()  # Write your query here