from sqlalchemy import Column, Integer, String, Boolean

from database import Base


# TODO: Pydantic model 사용 고려해보기
class Buyer(Base):
    __tablename__ = "buyer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    is_active = Column(Boolean, default=True)
    description = Column(String)


class Seller(Base):
    __tablename__ = "seller"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    is_active = Column(Boolean, default=True)
    description = Column(String)


class Property(Base):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    type = Column(String)  # FIXME to enum
    is_active = Column(Boolean, default=True)
    description = Column(String)
