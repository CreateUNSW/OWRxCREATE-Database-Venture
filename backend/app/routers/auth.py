import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi.security.http import HTTPBearer
import jwt

from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import HTTPBearer, HTTPBasicCredentials

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# db
from models import models, schema
from database.database import get_db
from sqlalchemy.orm import Session

# Password hashing
from hashlib import new, sha256

# Environment variables
load_dotenv()

expiryTimeMinutes = float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
secretJWT = os.getenv('JWT_SECRET')
algorithmJWT = os.getenv('JWT_ALGORITHM')
security = HTTPBearer()

# Creates a JWT token containing a payload combination of the user zid
# and expiry time of the token
def createToken(zid: str):
    payload = {
        "zid": zid,
        "expires": str(datetime.utcnow() + timedelta(minutes=expiryTimeMinutes))
    }

    token = jwt.encode(payload, secretJWT, algorithm=algorithmJWT)
    return token

# Given a JWT token, verifies the token against the secret key and
# returns the payload if it hasn't expired
def decodeToken(token: str):
    try:
        decodedToken = jwt.decode(token, secretJWT, algorithms=algorithmJWT)
        expires = datetime.strptime(decodedToken['expires'], "%Y-%m-%d %H:%M:%S.%f")
        
        if expires >= datetime.utcnow():
            return decodedToken
        else:
            raise jwt.ExpiredSignatureError
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")

# Dependency injection for routes that need to be protected.
# Automatically parses the header for an authorisation token.
# If the token is invalid, an exception is created and sent
# to the client (via the decodeToken function)
def authorise(token: HTTPBasicCredentials = Depends(security)):
    return decodeToken(token.credentials)


# Default role for a new user is 'member'
@router.post('/register/', response_model=schema.Person)
def register(person: schema.RegisterRequest, db: Session = Depends(get_db)):
    # Check if zid already registered
    userExists = db.query(models.Person).filter(
        models.Person.zid == person.zid
    ).first()

    if userExists:
        raise HTTPException(status_code=400, detail="User already exists")
    
    try:
        newUser = models.Person(
            zid = person.zid,
            password = encrypt(person.password),
            first_name = person.first_name,
            last_name = person.last_name,
            email = person.email,
            phone = person.phone,
            picture = person.picture,
            role = models.RoleType(2) if None else person.role
        )

        db.add(newUser)
        db.commit()
        # Without the password (handled by person response_model)
        return person
    except:
        raise HTTPException(status_code=402, detail="ERROR")

# Passes JWT token in response once a user is successfully logged in
@router.post('/login', response_model=schema.LoginResponse)
def login(person: schema.LoginRequest, db: Session = Depends(get_db)):
    # Ensure zid and password correct
    user = authenticateUser(person, db)

    if user:
        return {
            "success": True,
            "token": createToken(person.zid)
        }

    raise HTTPException(status_code=401, detail="Invalid username or password")

# Database returns None if user credentials do not match
def authenticateUser(person: schema.PersonCredentials, db: Session = Depends(get_db)):
    return db.query(models.Person).filter(
                models.Person.zid == person.zid,
                models.Person.password == encrypt(person.password)
            ).first()

# Test protected route
@router.get('/secret')
def secret(authorise: str = Depends(authorise)):
    return "secret resource"

# Encrypt user password and return the hexadecimal representation
def encrypt(password) :
    return sha256(password.encode()).hexdigest()