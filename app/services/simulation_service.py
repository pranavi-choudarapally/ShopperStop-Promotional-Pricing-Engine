from app.config.database import SessionLocal
from app.services.discount_engine import calculate_discount


class SimulationService:

    @staticmethod
    def simulate(request):

        db = SessionLocal()

        try:

            total_amount = 0

            for item in request.cart.items:
                total_amount += item.quantity * item.unit_price

            result = calculate_discount(
                amount=total_amount,
                tier=request.customer.tier,
                coupon_code=request.coupon_code,
                db=db
            )

            savings_percentage = 0

            if result["gross_amount"] > 0:
                savings_percentage = round(
                    (result["discount"] / result["gross_amount"]) * 100,
                    2
                )

            return {

                "gross_amount": result["gross_amount"],

                "total_discount": result["discount"],

                "net_amount": result["net_amount"],

                "discounts_applied": result["discounts_applied"],

                "savings_summary": {

                    "you_saved": result["discount"],

                    "savings_percentage": savings_percentage

                }

            }

        finally:
            db.close()