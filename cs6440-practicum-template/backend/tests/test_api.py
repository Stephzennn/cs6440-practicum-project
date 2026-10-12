import pytest
from fastapi.testclient import TestClient

import main
from synthea import SAMPLE_DATA_DIR, load_data


@pytest.fixture
def client(monkeypatch):
    """Always test against the bundled sample data, regardless of what's downloaded locally."""
    main.data.cache_clear()
    monkeypatch.setattr(main, "data", lambda: load_data(SAMPLE_DATA_DIR))
    return TestClient(main.app)


def test_health(client):
    body = client.get("/api/health").json()
    assert body["status"] == "ok"
    assert body["patients"] == 3


def test_search_patients(client):
    results = client.get("/api/patients", params={"q": "kris"}).json()
    assert [p["name"] for p in results] == ["Jacinto644 Kris249"]


def test_get_patient(client):
    pid = "a1f0c9e2-0001-4b6e-9a51-000000000001"
    body = client.get(f"/api/patients/{pid}").json()
    assert body["gender"] == "M"
    assert len(body["conditions"]) == 3


def test_unknown_patient_404(client):
    assert client.get("/api/patients/nope").status_code == 404
