from sqlalchemy import Column, Integer, String
from app.config.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, unique=True)
    tier = Column(String)