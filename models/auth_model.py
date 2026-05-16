from typing import Optional
from pydantic import BaseModel, EmailStr

class AuthLoginResponse(BaseModel):
    access_token: str
    refresh_token: str

class AuthLoginResponseInvalid(BaseModel):
    message: str
    statusCode: int

class AuthLoginRequest(BaseModel):
    email: str
    password: str

class AuthProfileResponse(BaseModel):
    id: int
    email: EmailStr
    password: str
    name: str
    role: str
    avatar: str