from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.coupon_schema import CouponCreate
from app.services.coupon_service import CouponService
from app.config.database import SessionLocal

router = APIRouter(
    prefix="/api/v1/coupons",
    tags=["Coupons"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_coupon(
    request: CouponCreate,
    db: Session = Depends(get_db)
):
    return CouponService.create_coupon(db, request)


@router.get("")
def get_all_coupons(
    db: Session = Depends(get_db)
):
    return CouponService.get_all_coupons(db)


@router.get("/{coupon_id}")
def get_coupon_by_id(
    coupon_id: int,
    db: Session = Depends(get_db)
):
    return CouponService.get_coupon_by_id(
        db,
        coupon_id
    )


@router.put("/{coupon_id}")
def update_coupon(
    coupon_id: int,
    request: CouponCreate,
    db: Session = Depends(get_db)
):
    return CouponService.update_coupon(
        db,
        coupon_id,
        request
    )


@router.delete("/{coupon_id}")
def delete_coupon(
    coupon_id: int,
    db: Session = Depends(get_db)
):
    return CouponService.delete_coupon(
        db,
        coupon_id
    )