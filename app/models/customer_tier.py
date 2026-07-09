from sqlalchemy import Column, Integer, String
from app.config.database import Base


class CustomerTier(Base):
    __tablename__ = "customer_tiers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=False)

    first_slab = Column(Integer, nullable=False)

    second_slab = Column(Integer, nullable=False)

    third_slab = Column(Integer, nullable=False)