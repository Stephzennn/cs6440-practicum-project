from fastapi import FastAPI

from data import DATA_DIR

app = FastAPI()


# All routes must start with /api
@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "synthea_data_found": (DATA_DIR / "patients.csv").exists(),
    }


# Add your endpoints below
