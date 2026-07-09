from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    # FLAT / PERCENTAGE / CATEGORY
    discount_type = Column(String, nullable=False)

    discount_value = Column(Integer, nullable=False)

    minimum_purchase = Column(Integer, nullable=False)

    # Used only for CATEGORY discounts
    category = Column(String, nullable=True)

    active = Column(Boolean, default=True)