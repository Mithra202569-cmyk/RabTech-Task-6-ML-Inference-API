
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_positive_sentiment():
    response = client.post(
        "/predict",
        json={"text": "This movie was amazing and wonderful!"}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["Positive", "Negative"]
    assert 0 <= response.json()["probability"] <= 1


def test_negative_sentiment():
    response = client.post(
        "/predict",
        json={"text": "This movie was boring and terrible."}
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["Positive", "Negative"]


def test_empty_text():
    response = client.post(
        "/predict",
        json={"text": "   "}
    )
    assert response.status_code == 200
    assert "error" in response.json()
