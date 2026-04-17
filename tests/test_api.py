import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health_check():
    """Verify the production health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "timestamp" in response.json()

def test_root_redirect():
    """Verify that root redirects to Swagger docs."""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

def test_predict_success():
    """
    Test the prediction endpoint.
    Note: This requires the model to be trained and located in the models/ dir.
    """
    response = client.post(
        "/predict",
        json={"skill": "TensorFlow"}
    )
    # Even if model is not loaded, API should return 200 with a 'Model not loaded' message
    assert response.status_code == 200
    data = response.json()
    assert "skill" in data
    assert "classification" in data
    assert "confidence" in data
