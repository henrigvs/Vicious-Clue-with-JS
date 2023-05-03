import json
from flask import Blueprint, render_template, session, redirect, url_for

from src.application.form.RiddleForm import RiddleForm
from src.application.service.RiddleService import RiddleService

createRiddleBP = Blueprint('createRiddle', __name__)


@createRiddleBP.route("/", methods=['GET', 'POST'])
def createRiddle():
    form = RiddleForm()
    ownerId = session['userId']

    if form.validate_on_submit():
        # Fetch riddle details from form
        description = form.description.data
        solution = form.solution.data
        difficulty = form.difficulty.data
        clueJSON = form.clues.data
        clues = json.loads(clueJSON)
        category = form.category.data

        # Call riddle API with JSON payload to add riddle in DB
        response = RiddleService.addRiddle(description, solution, clues, difficulty, ownerId, category)
        riddle = response.json()
        if response.status_code == 201:
            return render_template('riddles/creation_confirmation.html',
                                   riddle=riddle)
        else:
            return render_template(url_for('app.page_not_found'), errorMessage=response.json()['message'])

    else:
        if session.get('userIsConnected') is None:
            return redirect(url_for('login.loginUser'))
        else:
            return render_template('riddles/create.html', form=form)
