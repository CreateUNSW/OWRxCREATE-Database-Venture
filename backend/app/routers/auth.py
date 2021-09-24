import os
from dotenv import load_dotenv
import time
from jose import jwt

from fastapi import Depends, HTTPException, APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# db
from models import models, pydantic
from database.database import get_db
from sqlalchemy.orm import Session

# Password hashing
from hashlib import new, sha256

# Environment variables
load_dotenv()

expiryTimeMinutes = float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
secretJWT = os.getenv('JWT_SECRET')
algorithmJWT = os.getenv('JWT_ALGORITHM')

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
@router.post('/person/', response_model=pydantic.Person)
def createPerson(person: pydantic.PersonRegister, db: Session = Depends(get_db)):
    # Check if zid already registered
    userExists = db.query(models.Person).filter(models.Person.zid == person.zid).first()
    if userExists:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashedPassword = encrypt(person.password)
    newPerson = models.Person(
        zid = person.zid,
        password = hashedPassword,
        first_name = person.first_name,
        last_name = person.last_name,
        email = person.email,
        phone = person.phone,
        picture = person.picture,
        role = models.RoleType(1)
    )

    db.add(newPerson)
    db.commit()

    # Without the password (handled by person response_model)
    return person

def getPersonByZid(zid, db: Session = Depends(get_db)):
    return db.query(models.Person).filter(models.Person.zid == zid).first()


# Encrypt user password and return the hexadecimal representation
def encrypt(password) :
    return sha256(password.encode()).hexdigest()