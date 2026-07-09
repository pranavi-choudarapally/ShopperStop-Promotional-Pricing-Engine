from sqlalchemy.orm import Session

from app.models.customer_tier import CustomerTier


class CustomerTierService:

    @staticmethod
    def create_tier(db: Session, request):

        tier = CustomerTier(
            name=request.name,
            first_slab=request.first_slab,
            second_slab=request.second_slab,
            third_slab=request.third_slab
        )

        db.add(tier)
        db.commit()
        db.refresh(tier)

        return tier

    @staticmethod
    def get_all_tiers(db: Session):

        return db.query(CustomerTier).all()

    @staticmethod
    def update_tier(db: Session, tier_id: int, request):

        tier = db.query(CustomerTier).filter(
            CustomerTier.id == tier_id
        ).first()

        if tier is None:
            return {
                "message": "Customer Tier not found"
            }

        tier.name = request.name
        tier.first_slab = request.first_slab
        tier.second_slab = request.second_slab
        tier.third_slab = request.third_slab

        db.commit()
        db.refresh(tier)

        return tier