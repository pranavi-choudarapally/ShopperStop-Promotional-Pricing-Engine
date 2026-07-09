from fastapi import FastAPI

from app.schemas.bill_schema import BillRequest

from app.config.database import engine, Base

from app.models import customer
from app.models import promotion
from app.models import bill
from app.models import coupon
from app.models import customer_tier

from app.services.bill_service import BillService

from app.routers import promotion_router
from app.routers import coupon_router
from app.routers import customer_tier_router
from app.routers import simulation_router
from app.routers import health_router

app = FastAPI(
    title="ShopperStop Promotional Pricing Engine",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(promotion_router.router)
app.include_router(coupon_router.router)
app.include_router(customer_tier_router.router)
app.include_router(simulation_router.router)
app.include_router(health_router.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to ShopperStop Promotional Pricing Engine"
    }


@app.post("/api/v1/bills/calculate")
def calculate_bill(request: BillRequest):
    return BillService.calculate_bill(request)