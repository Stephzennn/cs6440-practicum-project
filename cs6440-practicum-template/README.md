# Project Name

Short description of what this app does.

**Stack:** React (frontend) + FastAPI (backend), using [Synthea](https://synthetichealth.github.io/downloads.html) synthetic patient data. Deploys to Vercel.

## Run locally

```bash
# Terminal 1 – backend
cd backend
pip install -e ".[dev]"
uvicorn main:app --reload --port 8000

# Terminal 2 – frontend
cd frontend
npm install
npm run dev
```

Open http://localhost:5173.

## Get the real data

The app starts with 3 sample patients. To load Synthea's 100-patient set:

```bash
python scripts/download_synthea.py
```

## Deploy

Import the repo into [Vercel](https://vercel.com/new). `vercel.json` handles the rest.

## Where things are

- `frontend/src/` – React page
- `backend/main.py` – API routes
- `backend/synthea.py` – reads the data
