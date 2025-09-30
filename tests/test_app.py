import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_sum():
    r = client.post("/sum", json={"a": 1.5, "b": 2.5})
    assert r.status_code == 200
    assert r.json()["sum"] == 5.0
