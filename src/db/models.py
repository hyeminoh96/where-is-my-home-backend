from sqlalchemy import Column, Integer, String, Boolean

from src.db.database import Base


class Buyer(Base):
    __tablename__ = "buyer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    phone_number = Column(String(20))
    address = Column(String(50))
    is_active = Column(Boolean, default=True)
    description = Column(String(100))


class Seller(Base):
    __tablename__ = "seller"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    phone_number = Column(String(20))
    address = Column(String(50))
    is_active = Column(Boolean, default=True)
    description = Column(String(100))


class Property(Base):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(50))
    type = Column(String(20))  # FIXME to enum
    is_active = Column(Boolean, default=True)
    description = Column(String(100))
    # TODO: owner_id relation 설정
