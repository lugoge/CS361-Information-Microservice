import json
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_info_valid_context(client):
    response = client.get("/info/add_customer_lugoge")

    assert response.status_code == 200

    data = response.get_json()
    assert data["context"] == "add_customer_lugoge"
    assert "title" in data
    assert "purpose" in data
    assert "steps" in data


def test_get_info_invalid_context(client):
    response = client.get("/info/nonexistent_context")

    assert response.status_code == 404

    data = response.get_json()
    assert data is not None
    assert "error" in data


def test_list_available_contexts(client):
    response = client.get("/info")

    assert response.status_code == 200

    data = response.get_json()
    assert "available_contexts" in data
    assert isinstance(data["available_contexts"], list)
