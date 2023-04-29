from flask import Blueprint, request, render_template, redirect, url_for
import requests
from resources.config.properties import HOST, PORT

editBP = Blueprint('edit', __name__)


@editBP.route('/<riddleId>', methods=['GET', 'POST'])
def editRiddle(riddleId):
    if request.method == 'POST':
        description = request.form['description']
        solution = request.form['solution']
        clue = request.form['clue']
        difficulty = request.form['difficulty']

        # Retrieve the owner Id from DB
        ownerId = requests.get(f"http://{HOST}:{PORT}/riddles/riddle/{riddleId}").json()['ownerId']

        json = {
            'description': description,
            'solution': solution,
            'clue': clue,
            'difficulty': int(difficulty),
            'ownerId': ownerId
        }

        try:
            response = requests.put(f"http://{HOST}:{PORT}/riddles/edit/{riddleId}", json=json)
            if response.status_code == 200:
                return redirect(url_for('list.getList'))
            else:
                errorMessage = 'Error updating riddle.'
        except Exception as e:
            errorMessage = 'Error updating riddle.'
            print(e)
        return render_template('riddles/edit.html', error_message=errorMessage, riddle=json)
    else:
        data = requests.get(f"http://{HOST}:{PORT}/riddles/riddle/{riddleId}")
        if data.status_code != 200:
            return "Error: Unable to fetch data", 500
        riddle = data.json()
        return render_template('riddles/edit.html', riddle=riddle)


@editBP.route('/delete/<riddleId>', methods=['POST'])
def deleteRiddle(riddleId):
    try:
        response = requests.delete(f"http://{HOST}:{PORT}/riddles/delete/{riddleId}")
        if response.status_code == 200:
            return redirect(url_for('list.getList'))
        else:
            error_message = 'Error deleting riddle.'
    except Exception as e:
        error_message = 'Error deleting riddle.'
        print(e)
