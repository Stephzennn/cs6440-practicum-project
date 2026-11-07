from fastapi import APIRouter
from pydantic import BaseModel

from services.glucose_analysis import glucose_summary

router = APIRouter(prefix="/api/glucose", tags=["Glucose"])


class GlucoseRequest(BaseModel):
    readings: list[float]


@router.post("/summary")
def calculate_summary(request: GlucoseRequest):
    return glucose_summary(request.readings)
