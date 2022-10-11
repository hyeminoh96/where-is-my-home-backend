from typing import List, Union
from pydantic import BaseModel


class PropertyBase(BaseModel):
    address: str
    type: str
    is_active: bool
    description: Union[str, None] = None


class PropertyCreate(PropertyBase):
    pass


class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    phone_number: str
    address: str
    is_active: bool
    description: Union[str, None] = None


class UserCreate(UserBase):
    pass


class Buyer(UserBase):
    id: int

    class Config:
        orm_mode = True


class Seller(UserBase):
    id: int

    class Config:
        orm_mode = True
