from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "username": "abcd",
                "password": "1234567"
            }
        }