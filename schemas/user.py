from typing import Optional, Any

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    _id: Optional[Any] = None
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserCreate(UserBase):
    name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserUpdate(UserBase):
    password: Optional[str] = None


class Auth(UserBase):
    email: EmailStr
    password: str
