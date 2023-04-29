import requests

from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray
from resources.config.properties import HOST, PORT


class JSONGetter:

    @staticmethod
    def getRiddlesJSON():
        riddlesResponse = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddles")
        riddles = convertJSONToERiddlesArray(riddlesResponse.json())
        return riddles
