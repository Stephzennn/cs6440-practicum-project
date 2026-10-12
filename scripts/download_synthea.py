#!/usr/bin/env python3
"""Download Synthea's 100-patient CSV sample into backend/data/synthea/.

Source: https://synthetichealth.github.io/downloads.html  (synthetic data, no PHI)

Usage:
    python scripts/download_synthea.py                       # patients, conditions, observations
    python scripts/download_synthea.py --tables all          # every CSV in the export
    python scripts/download_synthea.py --tables patients encounters medications
"""

from __future__ import annotations

import argparse
import io
import shutil
import urllib.request
import zipfile
from pathlib import Path

URL = (
    "https://synthetichealth.github.io/synthea-sample-data/downloads/latest/"
    "synthea_sample_data_csv_latest.zip"
)
DEST = Path(__file__).resolve().parents[1] / "backend" / "data" / "synthea"
DEFAULT_TABLES = ["patients", "conditions", "observations"]


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--tables", nargs="+", default=DEFAULT_TABLES,
                        help="CSV names to keep (without .csv), or 'all'")
    parser.add_argument("--url", default=URL, help="override the download URL")
    args = parser.parse_args()

    print(f"Downloading {args.url} ...")
    with urllib.request.urlopen(args.url) as resp:
        archive = zipfile.ZipFile(io.BytesIO(resp.read()))

    DEST.mkdir(parents=True, exist_ok=True)
    keep_all = args.tables == ["all"]
    kept = []
    for member in archive.namelist():
        name = Path(member).name
        if not name.endswith(".csv"):
            continue
        if keep_all or name.removesuffix(".csv") in args.tables:
            with archive.open(member) as src, open(DEST / name, "wb") as dst:
                shutil.copyfileobj(src, dst)
            kept.append(name)

    for name in sorted(kept):
        size_mb = (DEST / name).stat().st_size / 1e6
        print(f"  {name:<24} {size_mb:6.1f} MB")
    print(f"Saved {len(kept)} file(s) to {DEST}")


if __name__ == "__main__":
    main()
