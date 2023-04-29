import pytest
from flask import Flask

from src.riddles.api.controller.RiddleController import riddleBP


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(riddleBP, url_prefix="/riddles")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def deleteRiddle(client, riddleId: str):
    client.delete(f"/riddles/delete/{riddleId}")


def test_addRiddle(client):
    data = {
        'description': "What has keys but can't open locks?",
        'solution': "piano",
        'clue': "It's a musical instrument",
        'difficulty': 1,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    assert response.status_code == 201
    client.delete(f"/riddles/delete/{response.json['riddleId']}")


def test_deleteRiddle(client):
    data = {
        'description': "What has keys but can't open locks?",
        'solution': "piano",
        'clue': "It's a musical instrument",
        'difficulty': 1,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    riddleId = response.json['riddleId']

    response = client.delete(f"/riddles/delete/{riddleId}")

    assert response.status_code == 200


def test_editRiddle(client):
    data = {
        'description': "What has keys but can't open locks?",
        'solution': "piano",
        'clue': "It's a musical instrument",
        'difficulty': 1,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    riddleId = response.json['riddleId']

    data = {
        'description': "edited",
        'solution': "edited",
        'clue': "edited",
        'difficulty': 0,
        'ownerId': "adminId"
    }
    response = client.put(f"/riddles/edit/{riddleId}", json=data)
    assert response.status_code == 200
    assert response.json['description'] == "edited"
    assert response.json['solution'] == "edited"
    assert response.json['clue'] == "edited"
    assert response.json['difficulty'] == 0

    client.delete(f"/riddles/delete/{riddleId}")


def test_getAllRiddles(client):
    data = {
        'description': "What has keys but can't open locks?",
        'solution': "piano",
        'clue': "It's a musical instrument",
        'difficulty': 1,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    riddleId1 = response.json['riddleId']

    data = {
        'description': "description 2",
        'solution': "solution 2",
        'clue': "clue 2",
        'difficulty': 0,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    riddleId2 = response.json['riddleId']

    response = client.get("/riddles/getAllRiddles")

    assert response.status_code == 200
    assert len(response.json) == 11  # There is already 3 elements in the memory

    deleteRiddle(client, riddleId1)
    deleteRiddle(client, riddleId2)


def test_getRiddleById(client):
    data = {
        'description': "What has keys but can't open locks?",
        'solution': "piano",
        'clue': "It's a musical instrument",
        'difficulty': 1,
        'ownerId': "adminId"
    }
    response = client.post("/riddles/addRiddle", json=data)
    riddleId = response.json['riddleId']

    response = client.get(f"/riddles/riddle/{riddleId}")

    assert response.json['riddleId'] == riddleId
    assert response.json['description'] == "What has keys but can't open locks?"
    assert response.json['solution'] == "piano"
    assert response.json['clue'] == "It's a musical instrument"
    assert response.json['difficulty'] == 1
