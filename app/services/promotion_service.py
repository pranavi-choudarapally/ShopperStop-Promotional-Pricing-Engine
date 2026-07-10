from sqlalchemy.orm import Session

from app.models.promotion import Promotion


class PromotionService:

    # -------------------------------------------------
    # Create Promotion
    # -------------------------------------------------

    @staticmethod
    def create_promotion(db: Session, request):

        promotion = Promotion(

            name=request.name,

            description=request.description,

            promotion_type=request.promotion_type,

            discount_type=request.discount_type,

            discount_value=request.discount_value,

            minimum_purchase=request.minimum_purchase,

            category=request.category,

            buy_quantity=request.buy_quantity,

            free_quantity=request.free_quantity,

            applicable_sku=request.applicable_sku,

            applicable_store=request.applicable_store,

            start_time=request.start_time,

            end_time=request.end_time,

            priority=request.priority,

            stackable=request.stackable,

            usage_limit=request.usage_limit,

            active=request.active

        )

        db.add(promotion)

        db.commit()

        db.refresh(promotion)

        return promotion

    # -------------------------------------------------
    # Get All Promotions
    # -------------------------------------------------

    @staticmethod
    def get_all_promotions(db: Session):

        return db.query(Promotion).all()

    # -------------------------------------------------
    # Get Promotion By ID
    # -------------------------------------------------

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

    # -------------------------------------------------
    # Update Promotion
    # -------------------------------------------------

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

        promotion.description = request.description

        promotion.promotion_type = request.promotion_type

        promotion.discount_type = request.discount_type

        promotion.discount_value = request.discount_value

        promotion.minimum_purchase = request.minimum_purchase

        promotion.category = request.category

        promotion.buy_quantity = request.buy_quantity

        promotion.free_quantity = request.free_quantity

        promotion.applicable_sku = request.applicable_sku

        promotion.applicable_store = request.applicable_store

        promotion.start_time = request.start_time

        promotion.end_time = request.end_time

        promotion.priority = request.priority

        promotion.stackable = request.stackable

        promotion.usage_limit = request.usage_limit

        promotion.active = request.active

        promotion.version += 1

        db.commit()

        db.refresh(promotion)

        return promotion

    # -------------------------------------------------
    # Soft Delete
    # -------------------------------------------------

    @staticmethod
    def delete_promotion(db: Session, promotion_id: int):

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

            "message": "Promotion deactivated (Soft Delete)"

        }

    # -------------------------------------------------
    # Activate Promotion
    # -------------------------------------------------

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

        db.refresh(promotion)

        return promotion

    # -------------------------------------------------
    # Deactivate Promotion
    # -------------------------------------------------

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

        db.refresh(promotion)

        return promotion