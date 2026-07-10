from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    DateTime
)

from datetime import datetime

from app.config.database import Base


class Promotion(Base):

    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)

    # -----------------------------
    # Basic Information
    # -----------------------------

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    # CATEGORY / BUY_X_GET_Y / FLAT / PERCENTAGE / TIME_BASED
    promotion_type = Column(String, nullable=False)

    # FLAT / PERCENTAGE / FREE_ITEM
    discount_type = Column(String, nullable=False)

    discount_value = Column(Float, nullable=False)

    minimum_purchase = Column(Float, default=0)

    # -----------------------------
    # Category Promotion
    # -----------------------------

    category = Column(String, nullable=True)

    # -----------------------------
    # Buy X Get Y
    # -----------------------------

    buy_quantity = Column(Integer, nullable=True)

    free_quantity = Column(Integer, nullable=True)

    # -----------------------------
    # Product & Store
    # -----------------------------

    applicable_sku = Column(String, nullable=True)

    applicable_store = Column(String, nullable=True)

    # -----------------------------
    # Scheduling
    # -----------------------------

    start_time = Column(DateTime, nullable=True)

    end_time = Column(DateTime, nullable=True)

    # -----------------------------
    # Rule Engine
    # -----------------------------

    priority = Column(Integer, default=1)

    stackable = Column(Boolean, default=True)

    usage_limit = Column(Integer, nullable=True)

    # -----------------------------
    # Status
    # -----------------------------

    active = Column(Boolean, default=True)

    version = Column(Integer, default=1)

    # -----------------------------
    # Audit
    # -----------------------------

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )