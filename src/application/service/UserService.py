import requests
from requests import Response

from resources.config.properties import HOST, PORT


class UserService:

    @staticmethod
    def loginUser(email: str, password: str) -> Response:
        payload = {
            "email": email,
            "password": password
        }
        return requests.put(f"http://{HOST}:{PORT}/users/login", json=payload)

    @staticmethod
    def logoutUser(userId: str) -> Response:
        return requests.put(f"http://{HOST}:{PORT}/users/{userId}/logout")

    @staticmethod
    def addUser(firstName: str, lastName: str, email: str, password: str, role: str) -> Response:
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "role": role
        }
        return requests.post(f"http://{HOST}:{PORT}/users/addUser", json=payload)

    @staticmethod
    def editUser(userId: str, firstName: str, lastName: str, email: str, password: str, role: str,
                 isConnected: str, bestScore: int) -> Response:
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "role": role,
            "isConnected": isConnected,
            "bestScore": bestScore
        }
        return requests.put(f"http://{HOST}:{PORT}/users/edit/{userId}", json=payload)

    @staticmethod
    def getUserById(userId: str) -> Response:
        return requests.get(f"http://{HOST}:{PORT}/users/{userId}")
