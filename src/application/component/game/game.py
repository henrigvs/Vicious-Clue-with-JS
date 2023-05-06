from flask import Blueprint, render_template, session, redirect, url_for

from application.static_methods import JSONToERiddles
from resources.config.properties import HOST, PORT
import requests

gameBP = Blueprint('game', __name__)
pointer = 1


def getRiddleJSON():  # Retrieve list of riddles from the getAllRiddles endpoint
    riddlesResponse = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddles")
    riddles = JSONToERiddles.convertJSONToERiddlesArray(riddlesResponse.json())
    return riddles


@gameBP.route('/', methods=['GET'])
def game():
    if session.get('userIsConnected'):
        return render_template('riddles/game.html', userId=session.get('userId'))
    else:
        return redirect(url_for('game.demoGame'))


@gameBP.route('demoGame', methods=['GET'])
def demoGame():
    return render_template('riddles/demo_game.html')


@gameBP.route('demoGameCompleted', methods=['GET'])
def demoGameCompleted():
    return render_template('riddles/demo_completed.html')
