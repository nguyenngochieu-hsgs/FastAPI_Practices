from fastapi import APIRouter, HTTPException, Body
from dependencies.auth import signJWT
import schemas

fake_user = {
        id: 1,
        "name": "nguyen ngoc hieu",
        "username": "nnhieu",
        "email": "nnhieu0811@gmail.com",
        "password": "123456"
}


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses = {
        404: {"description": "Not Found"}
    }
) 

def check_user(data: schemas.UserLoginSchema):
    if fake_user["username"] == data.username and fake_user["password"] == data.password:
        return data

    return None

@router.post("/login")
async def login(user: schemas.UserLoginSchema = Body(...)):
    validate_user = check_user(user)
    if validate_user:
        return signJWT(user.username)
    
    return {
        "error": "wrong login details"
    }