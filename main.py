from datetime import timedelta
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth.user_model import User, get_current_user, fake_users_db, Token, \
    authenticate_user, create_access_token, get_current_active_user
from src.db import models, schemas, crud
from src.db.database import engine, SessionLocal

ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def say_hello(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# FIXME : root url

@app.get("/buyer", response_model=List[schemas.Buyer])
def read_buyers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    buyers = crud.get_buyers(db, skip=skip, limit=limit)
    return buyers


@app.get("/buyer/{buyer_id}", response_model=schemas.Buyer)
def read_buyer(buyer_id: int, db: Session = Depends(get_db)):
    buyer = crud.get_buyer(db, buyer_id=buyer_id)
    if buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return buyer


@app.post("/buyer", response_model=schemas.Buyer)
def create_buyer(buyer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    # TODO: existing validation
    return crud.create_buyer(db=db, buyer=buyer)


@app.put("/buyer/{buyer_id}")
def update_buyer(buyer_id: int = None):
    return {"update": {"buyer_id": buyer_id}}


@app.delete("/buyer/{buyer_id}")
def delete_buyer(buyer_id: int = None):
    return {"delete": {"buyer_id": buyer_id}}


@app.get("/seller", response_model=List[schemas.Seller])
def read_sellers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sellers = crud.get_sellers(db, skip=skip, limit=limit)
    return sellers


@app.get("/seller/{seller_id}", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = crud.get_seller(db, seller_id=seller_id)
    if seller is None:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller


@app.post("/seller", response_model=schemas.Seller)
def create_seller(seller: schemas.CustomerCreate, db: Session = Depends(get_db)):
    # TODO: existing validation
    return crud.create_seller(db=db, seller=seller)


@app.put("/seller/{seller_id}")
def update_seller(seller_id: int = None):
    return {"update": {"seller_id": seller_id}}


@app.delete("/seller/{seller_id}")
def delete_seller(seller_id: int = None):
    return {"delete": {"seller_id": seller_id}}


@app.get("/property", response_model=List[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=skip, limit=limit)
    return properties


@app.get("/property/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    _property = crud.get_property(db, property_id=property_id)
    if _property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return _property


@app.post("/property", response_model=schemas.Property)
def create_property(item: schemas.PropertyCreate, db: Session = Depends(get_db)):
    # TODO: existing validation
    return crud.create_property(db=db, _property=item)


@app.put("/property/{property_id}")
def update_property(property_id: int = None):
    return {"update": {"property_id": property_id}}


@app.delete("/property/{property_id}")
def delete_property(property_id: int = None):
    return {"delete": {"property_id": property_id}}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
