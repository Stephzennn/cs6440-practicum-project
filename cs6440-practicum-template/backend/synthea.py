"""Reads Synthea CSV files.

Uses backend/data/synthea/ if you've downloaded the real data, otherwise backend/data/sample/.
To use more tables or columns, add them to TABLES.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
REAL_DATA_DIR = HERE / "data" / "synthea"
SAMPLE_DATA_DIR = HERE / "data" / "sample"

# file name -> columns to load. Add tables/columns here as your project grows.
TABLES: dict[str, list[str]] = {
    "patients": ["ID", "BIRTHDATE", "DEATHDATE", "FIRST", "LAST", "GENDER", "CITY", "STATE"],
    "conditions": ["START", "STOP", "PATIENT", "CODE", "DESCRIPTION"],
    "observations": ["DATE", "PATIENT", "CODE", "DESCRIPTION", "VALUE", "UNITS"],
}


def _read(folder: Path, name: str, columns: list[str]) -> pd.DataFrame:
    path = folder / f"{name}.csv"
    if not path.exists():
        return pd.DataFrame(columns=columns)
    wanted = set(columns)
    df = pd.read_csv(path, usecols=lambda c: c.upper() in wanted, dtype=str)
    df.columns = [c.upper() for c in df.columns]
    return df.reindex(columns=columns)


def _age(birth: str, death: str | None) -> int | None:
    if pd.isna(birth):
        return None
    b = pd.to_datetime(birth).date()
    end = date.today() if pd.isna(death) else pd.to_datetime(death).date()
    return end.year - b.year - ((end.month, end.day) < (b.month, b.day))


def _records(df: pd.DataFrame) -> list[dict]:
    """DataFrame -> JSON-safe list of dicts (NaN becomes null)."""
    return json.loads(df.to_json(orient="records"))


@dataclass
class SyntheaData:
    source: str
    patients: pd.DataFrame
    conditions: pd.DataFrame
    observations: pd.DataFrame

    def summary(self) -> dict:
        return {
            "source": self.source,
            "patients": len(self.patients),
            "conditions": len(self.conditions),
            "observations": len(self.observations),
        }

    def search_patients(self, q: str = "", limit: int = 50) -> list[dict]:
        df = self.patients
        if q:
            names = (df["FIRST"].fillna("") + " " + df["LAST"].fillna("")).str.lower()
            df = df[names.str.contains(q.lower(), regex=False)]
        df = df.sort_values(["LAST", "FIRST"]).head(limit)
        return [
            {"id": r.ID, "name": f"{r.FIRST} {r.LAST}", "gender": r.GENDER,
             "age": _age(r.BIRTHDATE, r.DEATHDATE)}
            for r in df.itertuples()
        ]

    def get_patient(self, patient_id: str) -> dict | None:
        rows = self.patients[self.patients["ID"] == patient_id]
        if rows.empty:
            return None
        p = rows.iloc[0]
        conditions = self.conditions[self.conditions["PATIENT"] == patient_id]
        conditions = conditions.sort_values("START", ascending=False)
        return {
            "id": p["ID"],
            "name": f"{p['FIRST']} {p['LAST']}",
            "gender": p["GENDER"],
            "birthdate": p["BIRTHDATE"],
            "age": _age(p["BIRTHDATE"], p["DEATHDATE"]),
            "city": p["CITY"],
            "state": p["STATE"],
            "conditions": _records(
                conditions[["START", "STOP", "CODE", "DESCRIPTION"]].rename(columns=str.lower)
            ),
        }


def load_data(folder: str | Path | None = None) -> SyntheaData:
    if folder is None:
        folder = os.environ.get("SYNTHEA_DATA_DIR") or (
            REAL_DATA_DIR if (REAL_DATA_DIR / "patients.csv").exists() else SAMPLE_DATA_DIR
        )
    folder = Path(folder)
    if not (folder / "patients.csv").exists():
        raise FileNotFoundError(f"No patients.csv in {folder}")
    tables = {name: _read(folder, name, cols) for name, cols in TABLES.items()}
    source = "sample" if folder == SAMPLE_DATA_DIR else "synthea"
    return SyntheaData(source=source, **tables)
