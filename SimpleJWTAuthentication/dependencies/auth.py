from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException

import time
from typing import Dict

import jwt

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(username: str) -> Dict[str, str]:
    payload = {
        "username": username,
        "expires": time.time() + 600
    }
    
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None

    except:
        return {
            
        }

def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    try:
        payload = decodeJWT(http_authorization_credentials.credentials)

    except:
        payload = None
    
    if payload:
        return payload.get("username")
    
    raise HTTPException(
        status_code=403,
        detail="Vadilate not successfully"
    )