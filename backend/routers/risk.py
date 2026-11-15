from fastapi import APIRouter

from models.framingham.framingham import framingham_risk

router = APIRouter(prefix="/api/risk", tags=["Risk"])


@router.post("")
def calculate_risk(inputs: dict):
    risk = framingham_risk(inputs)
    return {"framingham": {"value": f"{risk * 100:.1f}%"}}
