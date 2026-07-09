from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, unique=True, nullable=False)

    discount_type = Column(String, nullable=False)

    discount_value = Column(Integer, nullable=False)

    minimum_purchase = Column(Integer, nullable=False)

    active = Column(Boolean, default=True)