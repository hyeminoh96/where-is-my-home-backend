from typing import Union
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


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    address: str
    is_active: bool
    description: Union[str, None] = None


class CustomerCreate(CustomerBase):
    pass


class Buyer(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class Seller(CustomerBase):
    id: int

    class Config:
        orm_mode = True
