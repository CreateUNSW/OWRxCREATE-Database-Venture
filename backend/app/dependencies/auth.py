import os
from dotenv import load_dotenv
import time
from jose import jwt

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

t = createToken(5)
print(decodeToken(t['accessToken']))