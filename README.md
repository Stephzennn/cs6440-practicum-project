# CS 6440 Practicum Project

React frontend + Python (FastAPI) backend, using [Synthea](https://synthetichealth.github.io/downloads.html) data. Hosted on Vercel.

## Run locally

```bash
# Terminal 1 – backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Terminal 2 – frontend
cd frontend
npm install
npm run dev
```

Open http://localhost:5173. It should say **Backend: connected**.

## Get the data

```bash
python scripts/download_synthea.py
```

Then in Python: `load_table("patients")` from `backend/data.py`.

## Where to add things

- Backend endpoints: `backend/main.py` (routes must start with `/api`)
- Frontend: `frontend/src/` — call the backend with `apiGet('/your-route')`

## Deploy

Import the repo at [vercel.com/new](https://vercel.com/new). No settings needed.
