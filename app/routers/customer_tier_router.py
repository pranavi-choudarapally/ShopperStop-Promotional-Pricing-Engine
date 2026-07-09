from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.schemas.customer_tier_schema import CustomerTierCreate
from app.services.customer_tier_service import CustomerTierService

router = APIRouter(
    prefix="/api/v1/customer-tiers",
    tags=["Customer Tiers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_customer_tier(
    request: CustomerTierCreate,
    db: Session = Depends(get_db)
):
    return CustomerTierService.create_tier(db, request)


@router.get("")
def get_customer_tiers(
    db: Session = Depends(get_db)
):
    return CustomerTierService.get_all_tiers(db)


@router.put("/{tier_id}")
def update_customer_tier(
    tier_id: int,
    request: CustomerTierCreate,
    db: Session = Depends(get_db)
):
    return CustomerTierService.update_tier(
        db,
        tier_id,
        request
    )