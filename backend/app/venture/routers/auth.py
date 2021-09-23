import os
from dotenv import load_dotenv
import time
from jose import jwt

from fastapi import Depends, HTTPException, APIRouter

router = APIRouter()

# db
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session

# Password hashing
from hashlib import sha256

# Environment variables
load_dotenv()

expiryTimeMinutes = float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
secretJWT = os.getenv('JWT_SECRET')
algorithmJWT = os.getenv('JWT_ALGORITHM')

from pydantic import BaseModel
# Pydantic Models for route response
class Person(BaseModel):
    zid: str
    password: str
    first_name: str
    last_name: str
    email: str
    phone: str
    picture: str
    role: str


def createToken(userId: str):
    payload = {
        "userId": userId,
        "expires": time.time() + expiryTimeMinutes * 60
    }

    token = jwt.encode(payload, secretJWT, algorithm=algorithmJWT)
    return { "accessToken": token }

def decodeToken(token: str):
    try:
        decodedToken = jwt.decode(token, secretJWT, algorithms=[algorithmJWT])
        return decodedToken if decodedToken['expires'] >= time.time() else None
    except:
        return None

# Add new person to the database
@router.post('/person/', response_model=Person, tags=["auth"])
def createPerson(person: Person, db: Session = Depends(get_db)):
    # Check if zid already registered
    userExists = db.query(models.Person).filter(models.Person.zid == person.zid).first()
    if userExists:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashedPassword_hi = encrypt(person.password)
    newPerson = models.Person(
        zid = person.zid,
        password = hashedPassword_hi,
        first_name = person.first_name,
        last_name = person.last_name,
        email = person.email,
        phone = person.phone,
        picture = person.picture,
        role = person.role
    )

    db.add(newPerson)
    db.commit()
    return newPerson

def getPersonByZid(zid, db: Session = Depends(get_db)):
    return db.query(models.Person).filter(models.Person.zid == zid).first()


# Encrypt user password and return the hexadecimal representation
def encrypt(password) :
    return sha256(password.encode()).hexdigest()