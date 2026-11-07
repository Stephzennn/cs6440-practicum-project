from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data" / "synthea"


def load_table(name: str) -> pd.DataFrame:
    """Load a Synthea CSV by name, e.g. load_table("patients")."""
    return pd.read_csv(DATA_DIR / f"{name}.csv")
