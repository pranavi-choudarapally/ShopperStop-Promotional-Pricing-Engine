from fastapi import APIRouter
from sqlalchemy import text
from app.config.database import SessionLocal

router = APIRouter(
    prefix="/api/v1",
    tags=["Health"]
)


@router.get("/health")
def health_check():

    db = SessionLocal()

    try:

        db.execute(text("SELECT 1"))

        database_status = "Connected"

    except Exception:

        database_status = "Disconnected"

    finally:

        db.close()

    return {

        "status": "UP",

        "application": "ShopperStop Promotional Pricing Engine",

        "version": "1.0.0",

        "database": database_status

    }