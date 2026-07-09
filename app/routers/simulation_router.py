from fastapi import APIRouter

from app.schemas.simulation_schema import SimulationRequest
from app.services.simulation_service import SimulationService

router = APIRouter(
    prefix="/api/v1/promotions",
    tags=["Promotion Simulation"]
)


@router.post("/simulate")
def simulate(request: SimulationRequest):

    return SimulationService.simulate(request)