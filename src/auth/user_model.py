from typing import Union

from fastapi import Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


def fake_decode_token(token):
    return User(username=token + "fake-decoded", email="john@example.com", full_name="John Doe")


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

