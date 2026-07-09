from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.promotion_schema import PromotionCreate
from app.services.promotion_service import PromotionService
from app.config.database import SessionLocal

router = APIRouter(
    prefix="/api/v1/promotions",
    tags=["Promotions"]
)


# ---------------- DATABASE DEPENDENCY ---------------- #

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- CREATE ---------------- #

@router.post("")
def create_promotion(
    request: PromotionCreate,
    db: Session = Depends(get_db)
):
    return PromotionService.create_promotion(db, request)


# ---------------- GET ALL ---------------- #

@router.get("")
def get_all_promotions(
    db: Session = Depends(get_db)
):
    return PromotionService.get_all_promotions(db)


# ---------------- GET BY ID ---------------- #

@router.get("/{promotion_id}")
def get_promotion_by_id(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    return PromotionService.get_promotion_by_id(
        db,
        promotion_id
    )


# ---------------- UPDATE ---------------- #

@router.put("/{promotion_id}")
def update_promotion(
    promotion_id: int,
    request: PromotionCreate,
    db: Session = Depends(get_db)
):
    return PromotionService.update_promotion(
        db,
        promotion_id,
        request
    )


# ---------------- DELETE ---------------- #

@router.delete("/{promotion_id}")
def delete_promotion(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    return PromotionService.delete_promotion(
        db,
        promotion_id
    )


# ---------------- ACTIVATE ---------------- #

@router.post("/{promotion_id}/activate")
def activate_promotion(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    return PromotionService.activate_promotion(
        db,
        promotion_id
    )


# ---------------- DEACTIVATE ---------------- #

@router.post("/{promotion_id}/deactivate")
def deactivate_promotion(
    promotion_id: int,
    db: Session = Depends(get_db)
):
    return PromotionService.deactivate_promotion(
        db,
        promotion_id
    )