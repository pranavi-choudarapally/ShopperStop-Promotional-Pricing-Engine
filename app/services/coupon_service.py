from sqlalchemy.orm import Session

from app.models.coupon import Coupon


class CouponService:

    @staticmethod
    def create_coupon(db: Session, request):

        coupon = Coupon(
            code=request.code,
            discount_type=request.discount_type,
            discount_value=request.discount_value,
            minimum_purchase=request.minimum_purchase,
            active=request.active
        )

        db.add(coupon)
        db.commit()
        db.refresh(coupon)

        return coupon

    @staticmethod
    def get_all_coupons(db: Session):

        return db.query(Coupon).all()

    @staticmethod
    def get_coupon_by_id(db: Session, coupon_id: int):

        return db.query(Coupon).filter(
            Coupon.id == coupon_id
        ).first()

    @staticmethod
    def update_coupon(db: Session, coupon_id: int, request):

        coupon = db.query(Coupon).filter(
            Coupon.id == coupon_id
        ).first()

        if coupon is None:
            return {"message": "Coupon not found"}

        coupon.code = request.code
        coupon.discount_type = request.discount_type
        coupon.discount_value = request.discount_value
        coupon.minimum_purchase = request.minimum_purchase
        coupon.active = request.active

        db.commit()
        db.refresh(coupon)

        return coupon

    @staticmethod
    def delete_coupon(db: Session, coupon_id: int):

        coupon = db.query(Coupon).filter(
            Coupon.id == coupon_id
        ).first()

        if coupon is None:
            return {"message": "Coupon not found"}

        db.delete(coupon)
        db.commit()

        return {
            "message": "Coupon deleted successfully"
        }