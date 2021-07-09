from fastapi.testclient import TestClient
from main import app
from datetime import datetime

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong","timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}



# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica","timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}

#Task 2 Writing Test Cases
# test to check the correct functioning of the /ping route
def test_joy():
    with TestClient(app) as client:
        response = client.get("/joy")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"joy":"Kolkata is called the city of Joy","timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}


def test_golden():
    with TestClient(app) as client:
        response = client.get("/golden")
        # asserting the correct responses is received
        assert response.status_code == 200
        assert response.json() == {"golden":"Life is Golden","timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
