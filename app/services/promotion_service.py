from sqlalchemy.orm import Session
from app.models.promotion import Promotion


class PromotionService:

    @staticmethod
    def create_promotion(db: Session, request):

        promotion = Promotion(
            name=request.name,
            discount_type=request.discount_type,
            discount_value=request.discount_value,
            minimum_purchase=request.minimum_purchase,
            active=request.active
        )

        db.add(promotion)
        db.commit()
        db.refresh(promotion)

        return promotion

    @staticmethod
    def get_all_promotions(db: Session):

        return db.query(Promotion).all()

    @staticmethod
    def get_promotion_by_id(db: Session, promotion_id: int):

        promotion = db.query(Promotion).filter(
            Promotion.id == promotion_id
        ).first()

        if not promotion:
            return {
                "message": "Promotion not found"
            }

        return promotion

    @staticmethod
    def update_promotion(db: Session, promotion_id: int, request):

        promotion = db.query(Promotion).filter(
            Promotion.id == promotion_id
        ).first()

        if not promotion:
            return {
                "message": "Promotion not found"
            }

        promotion.name = request.name
        promotion.discount_type = request.discount_type
        promotion.discount_value = request.discount_value
        promotion.minimum_purchase = request.minimum_purchase
        promotion.active = request.active

        db.commit()
        db.refresh(promotion)

        return promotion

    @staticmethod
    def delete_promotion(db: Session, promotion_id: int):

        promotion = db.query(Promotion).filter(
            Promotion.id == promotion_id
        ).first()

        if not promotion:
            return {
                "message": "Promotion not found"
            }

        db.delete(promotion)
        db.commit()

        return {
            "message": "Promotion deleted successfully"
        }

    @staticmethod
    def activate_promotion(db: Session, promotion_id: int):

        promotion = db.query(Promotion).filter(
            Promotion.id == promotion_id
        ).first()

        if not promotion:
            return {
                "message": "Promotion not found"
            }

        promotion.active = True

        db.commit()

        return {
            "message": "Promotion activated"
        }

    @staticmethod
    def deactivate_promotion(db: Session, promotion_id: int):

        promotion = db.query(Promotion).filter(
            Promotion.id == promotion_id
        ).first()

        if not promotion:
            return {
                "message": "Promotion not found"
            }

        promotion.active = False

        db.commit()

        return {
            "message": "Promotion deactivated"
        }