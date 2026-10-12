"""API routes. Keep every route under /api."""

from functools import lru_cache

from fastapi import FastAPI, HTTPException

from synthea import SyntheaData, load_data

app = FastAPI(title="CS 6440 Practicum API")


@lru_cache
def data() -> SyntheaData:
    """Load the CSVs once."""
    return load_data()


@app.get("/api/health")
def health():
    return {"status": "ok", **data().summary()}


@app.get("/api/patients")
def list_patients(q: str = "", limit: int = 50):
    return data().search_patients(q, limit)


@app.get("/api/patients/{patient_id}")
def get_patient(patient_id: str):
    patient = data().get_patient(patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# TODO: add your own endpoints here
