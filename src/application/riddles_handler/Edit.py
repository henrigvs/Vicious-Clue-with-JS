from flask import Blueprint, request, render_template, redirect, url_for, session
from resources.config.properties import HOST, PORT
import requests

editBP = Blueprint('edit', __name__)
allRiddles = []


@editBP.route('/<riddleId>', methods=['GET', 'POST'])
def editRiddle(riddleId):
    global allRiddles
    if request.method == 'POST':
        description = request.form['description']
        solution = request.form['solution']
        clue = request.form['clue']
        difficulty = request.form['difficulty']

        # Retrieve the ownerId from DB
        ownerId = requests.get(f"http://{HOST}:{PORT}/riddles/riddle/{riddleId}").json()['ownerId']

        json = {
            'description': description,
            'solution': solution,
            'clue': clue,
            'difficulty': int(difficulty),
            'ownerId': ownerId
        }

        response = requests.put(f"http://{HOST}:{PORT}/riddles/edit/{riddleId}", json=json)
        data = response.json()
        if response.status_code == 200:
            return redirect(url_for('list.getList'))
        elif response.status_code == 404:
            return render_template('error/404.html', errorMessage=data['message'])
        else:
            return render_template('error/errorHttp.html', errorCode=response.status_code)
    else:
        # Retrieve selected riddle
        response = requests.get(f"http://{HOST}:{PORT}/riddles/riddle/{riddleId}")
        if response.status_code == 404:
            return render_template('error/404.html')
        if response.status_code != 200:
            return render_template('error/errorHttp.html', errorCode=response.status_code)
        riddleSelected = response.json()

        # Retrieve all riddles id depending on admin or player (all or owned)
        allRiddlesId = _retrieveAllRiddles(session['userRole'])
        selectedRiddleId = riddleSelected['riddleId']
        # Find previous and next riddle IDs
        prevRiddleId = None
        nextRiddleId = None

        if riddleId in allRiddlesId:
            idx = allRiddlesId.index(selectedRiddleId)
            if idx > 0:
                prevRiddleId = allRiddlesId[idx - 1]
            if idx < len(allRiddlesId) - 1:
                nextRiddleId = allRiddlesId[idx + 1]

        # Return the web page with selected riddle and id of previous and next riddle (for navigating)
        return render_template('riddles/edit.html', riddle=riddleSelected, prevRiddleId=prevRiddleId, nextRiddleId=nextRiddleId)


@editBP.route('/delete/<riddleId>', methods=['POST'])
def deleteRiddle(riddleId):
    response = requests.delete(f"http://{HOST}:{PORT}/riddles/delete/{riddleId}")
    data = response.json()
    if response.status_code == 200:
        return redirect(url_for('list.getList'))
    elif response.status_code == 404:
        return render_template('error/404.html', message=data['message'])
    else:
        return render_template('error/errorHttp.html', errorCode=response.status_code,
                               errorMessage="Please contact the system admin")


def _retrieveAllRiddles(role: str):
    if role == "admin":
        response = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddles")
        data = response.json()
    elif role == "player":
        response = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddlesOf/{session['userId']}")
        data = response.json()
    else:
        return render_template('error/400.html', errorMessage="Something went wrong while identifying user role")

    # Storing only riddle id's
    riddle_ids = [riddle['riddleId'] for riddle in data]

    return riddle_ids


