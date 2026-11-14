# CS 6440 Practicum Project – Type 2 Diabetes Risk

Compare type 2 diabetes risk scores across published models (Framingham, QDiabetes, ADA, FINDRISC).

React frontend + FastAPI backend, using [Synthea](https://synthetichealth.github.io/downloads.html) synthetic data. Hosted on Vercel.

## Run the app

```powershell
# Terminal 1 – backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
cd backend
uvicorn main:app --reload --port 8000
```

```powershell
# Terminal 2 – frontend
cd frontend
npm install
npm run dev
```

Open http://localhost:5173. The API docs are at http://localhost:8000/docs.

Get the Synthea data (optional): `python scripts\download_synthea.py`

## Run a model on its own

```powershell
python backend\models\framingham\framingham.py
```

This uses the dummy patient in `backend/data/sample_patient.json` and prints the 8-year risk.

## Project structure

```
backend/
  main.py              FastAPI app (all routes start with /api)
  data.py              load_table("patients") for Synthea CSVs
  routers/             API endpoints
  services/            helper logic
  models/              one folder per risk model
frontend/
  src/components/      UI components (unstylized for now)
  src/sampleData.js    dummy values (replace with API calls later)
scripts/
  download_synthea.py  download the Synthea sample data
```

## Where to add things

- New model: add a folder under `backend/models/` and expose it through `backend/routers/risk.py`.
- New endpoint: add a router in `backend/routers/` and include it in `main.py`.
- Frontend: call the backend with `apiGet('/your-route')`.

## Deploy

Import the repo at [vercel.com/new](https://vercel.com/new). No settings needed.

## References

- Wilson PWF et al. Framingham Offspring Study. *Arch Intern Med.* 2007;167(10):1068-1074.
- Hippisley-Cox J, Coupland C. QDiabetes-2018. *BMJ.* 2017;359:j5019. (R code © University of Oxford, AGPL-3.0)
