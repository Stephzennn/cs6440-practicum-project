from fastapi import APIRouter, HTTPException
from data import load_table

router = APIRouter(prefix="/api/patients", tags=["Patients"])


@router.get("")
def get_patients(limit: int = 20):
    if not 1 <= limit <= 100:
        raise HTTPException(400, "limit must be between 1 and 100")

    try:
        df = load_table("patients")
    except FileNotFoundError:
        raise HTTPException(404, "patients.csv not found")

    return {
        "count": min(limit, len(df)),
        "patients": df.head(limit).fillna("").to_dict(orient="records")
    }


@router.get("/{patient_id}")
def get_patient(patient_id: str):
    try:
        df = load_table("patients")
    except FileNotFoundError:
        raise HTTPException(404, "patients.csv not found")

    patient = df[df["Id"].astype(str) == patient_id]

    if patient.empty:
        raise HTTPException(404, "Patient not found")

    return patient.fillna("").iloc[0].to_dict()
