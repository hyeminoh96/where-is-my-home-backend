from sqlalchemy.orm import Session

from src.db import models, schemas


def get_buyer(db: Session, buyer_id: int):
    return db.query(models.Buyer).filter(models.Buyer.id == buyer_id).first()


def get_buyers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Buyer).offset(skip).limit(limit).all()


def get_seller(db: Session, seller_id: int):
    return db.query(models.Seller).filter(models.Seller.id == seller_id).first()


def get_sellers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Seller).offset(skip).limit(limit).all()


def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()


def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()


def create_buyer(db: Session, buyer: schemas.CustomerCreate):
    new_buyer = models.Buyer(name=buyer.name, phone_number=buyer.phone_number, address=buyer.address,
                             is_active=buyer.is_active, description=buyer.description)
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return new_buyer


def create_seller(db: Session, seller: schemas.CustomerCreate):
    new_seller = models.Seller(name=seller.name, phone_number=seller.phone_number, address=seller.address,
                               is_active=seller.is_active, description=seller.description)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller


def create_property(db: Session, _property: schemas.PropertyCreate):
    new_property = models.Property(address=_property.address, type=_property.type,
                                   is_active=_property.is_active, description=_property.description)
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property
