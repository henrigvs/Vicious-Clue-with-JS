import requests
from flask import Blueprint, render_template, session, redirect, url_for

from resources.config.properties import HOST, PORT
from src.application.form.RiddleForm import CreateRiddleForm

createRiddleBP = Blueprint('createRiddle', __name__)


@createRiddleBP.route("/", methods=['GET', 'POST'])
def createRiddle():
    form = CreateRiddleForm()

    if form.validate_on_submit():
        description = form.description.data
        solution = form.solution.data
        clue = form.solution.data
        difficulty = form.difficulty.data
        ownerId = session['userId']

        payload = {
            "description": description,
            "solution": solution,
            "clue": clue,
            "difficulty": difficulty,
            "ownerId": ownerId
        }

        # Call riddle API with JSON payload to add riddle in DB
        response = requests.post(f"http://{HOST}:{PORT}/riddles/addRiddle", json=payload)
        if response.status_code == 201:
            return render_template('riddles/edit.html',
                                   error_message=None,
                                   riddle=payload
                                   )
        else:
            return render_template('error/400.html')

    else:
        if session.get('userIsConnected') is None:
            return redirect(url_for('login.loginUser'))
        else:
            return render_template('riddles/create.html', form=form)
