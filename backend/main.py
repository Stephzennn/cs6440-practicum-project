from fastapi import FastAPI
from routers import risk     
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
     # at the top, with the other imports
app.include_router(risk.router)   