from sqlalchemy import Column, Integer, Float, String
from app.config.database import Base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String)
    gross_amount = Column(Float)
    total_discount = Column(Float)
    net_amount = Column(Float)