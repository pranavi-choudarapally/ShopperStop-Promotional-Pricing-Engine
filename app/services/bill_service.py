from datetime import datetime

from app.services.discount_engine import calculate_discount
from app.config.database import SessionLocal
from app.utils.logger import logger


class BillService:

    @staticmethod
    def calculate_bill(request):

        db = SessionLocal()

        try:

            total_amount = 0

            for item in request.cart.items:
                total_amount += item.quantity * item.unit_price

            result = calculate_discount(
    amount=total_amount,
    tier=request.customer.tier,
    cart_items=request.cart.items,
    coupon_code=request.coupon_code,
    db=db
)

            savings_percentage = 0

            if result["gross_amount"] > 0:
                savings_percentage = round(
                    (result["discount"] / result["gross_amount"]) * 100,
                    2
                )

            # Log bill details
            logger.info(
                f"Bill generated | "
                f"Customer={request.customer.id} | "
                f"Gross={result['gross_amount']} | "
                f"Discount={result['discount']} | "
                f"Net={result['net_amount']}"
            )

            return {

                "bill_id": "BILL-" + datetime.now().strftime("%Y%m%d%H%M%S"),

                "customer_id": request.customer.id,

                "gross_amount": result["gross_amount"],

                "total_discount": result["discount"],

                "net_amount": result["net_amount"],

                "discounts_applied": result["discounts_applied"],

                "savings_summary": {

                    "you_saved": result["discount"],

                    "savings_percentage": savings_percentage

                },

                "calculated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            }

        finally:

            db.close()