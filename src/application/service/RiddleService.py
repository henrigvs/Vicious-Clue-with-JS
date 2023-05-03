from typing import List

import requests
from flask import render_template, url_for
from requests import Response

from resources.config.properties import HOST, PORT


class RiddleService:

    @staticmethod
    def addRiddle(description: str, solution: str, clues: List, difficulty: int, ownerId: str, category: str) -> Response:
        payload = {
            "description": description,
            "solution": solution,
            "clues": clues,
            "difficulty": difficulty,
            "ownerId": ownerId,
            "category": category,
        }
        return requests.post(f"http://{HOST}:{PORT}/riddles/addRiddle", json=payload)

    @staticmethod
    def editRiddle(riddleId: str, description: str, solution: str, clues: List, difficulty: int, ownerId: str, category: str) -> Response | str:
        payload = {
            "description": description,
            "solution": solution,
            "clues": clues,
            "difficulty": difficulty,
            "ownerId": ownerId,
            "category": category,
        }
        response = requests.put(f"http://{HOST}:{PORT}/riddles/edit/{riddleId}", json=payload)
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            return render_template(url_for('app.page_not_found'), errorMessage=response.json()['message'])
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code)

    @staticmethod
    def deleteRiddle(riddleId: str) -> Response | str:
        response = requests.delete(f"http://{HOST}:{PORT}/riddles/delete/{riddleId}")
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            return render_template(url_for('app.page_not_found'), errorMessage=response.json()['message'])
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code)

    @staticmethod
    def getAllRiddles() -> Response | str:
        response = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddles")
        if response.status_code == 200:
            return response
        else:
            return render_template('error/400.html', errorMessage="Something went wrong!")

    @staticmethod
    def getAllRiddlesOf(ownerId) -> Response | str:
        response = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddlesOf/{ownerId}")
        if response.status_code == 200:
            return response
        else:
            return render_template('error/400.html', errorMessage="Something went wrong!")

    @staticmethod
    def getRiddleById(riddleId) -> Response | str:
        response = requests.get(f"http://{HOST}:{PORT}/riddles/riddle/{riddleId}")
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            return render_template(url_for('app.page_not_found'), errorMessage=response.json()['message'])
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code)

    @staticmethod
    def increaseDifficulty(riddleId) -> Response | str:
        response = requests.post(f"http://{HOST}:{PORT}/riddles/increaseDifficulty/{riddleId}")
        if response.status_code == 200:
            return response
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code, errorMessage="Error updating difficulty")

    @staticmethod
    def decreaseDifficulty(riddleId) -> Response | str:
        response = requests.post(f"http://{HOST}:{PORT}/riddles/decreaseDifficulty/{riddleId}")
        if response.status_code == 200:
            return response
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code, errorMessage="Error updating difficulty")
