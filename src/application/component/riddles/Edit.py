from flask import Blueprint, request, render_template, redirect, url_for, session, jsonify

import requests
from src.application.form.RiddleForm import RiddleForm
import json

from src.application.service.RiddleService import RiddleService

editBP = Blueprint('edit', __name__)
allRiddles = []


@editBP.route('/<riddleId>', methods=['GET', 'POST'])
def editRiddle(riddleId):
    global allRiddles
    riddle = RiddleService.getRiddleById(riddleId).json()
    ownerId = riddle['ownerId']
    form = RiddleForm(submit_label="Edit Riddle")

    if form.validate_on_submit():
        # Fetch riddle from form
        description = form.description.data
        solution = form.solution.data
        difficulty = form.difficulty.data
        category = form.category.data
        cluesJSON = form.clues.data
        clues = json.loads(cluesJSON)

        # Call riddle API to edit riddle in DB
        RiddleService.editRiddle(riddleId, description, solution, clues, difficulty, ownerId, category)
        return redirect(url_for('list.getList'))


    else:
        # Retrieve all riddles id depending on admin or player (all or owned)
        allRiddlesId = _retrieveAllRiddles(session['userRole'])
        selectedRiddleId = riddle['riddleId']

        # Find previous and next riddle IDs
        prevRiddleId = None
        nextRiddleId = None
        if riddleId in allRiddlesId:
            idx = allRiddlesId.index(selectedRiddleId)
            if idx > 0:
                prevRiddleId = allRiddlesId[idx - 1]
            if idx < len(allRiddlesId) - 1:
                nextRiddleId = allRiddlesId[idx + 1]

        # Prefill the form with the riddle details

        form.description.data = riddle['description']
        form.solution.data = riddle['solution']
        form.clues.data = json.dumps(riddle['clues'])
        form.difficulty.data = riddle['difficulty']
        form.category.data = riddle['category']

        # Return the web page with selected riddle and id of previous and next riddle (for navigating)
        return render_template('riddles/edit.html',
                               form=form,
                               riddle=riddle,
                               prevRiddleId=prevRiddleId,
                               nextRiddleId=nextRiddleId,
                               clues=riddle['clues'])


@editBP.route('/deleteRiddle/<riddleId>', methods=['POST'])
def deleteRiddle(riddleId):
    RiddleService.deleteRiddle(riddleId)
    return "OK", 200


@editBP.route('/updateDifficulty/<riddleId>', methods=['POST'])
def updateDifficulty(riddleId):
    action = request.json['action']
    newDifficulty = None

    if action == "increase":
        newDifficulty = RiddleService.increaseDifficulty(riddleId).json()['difficulty']
    elif action == "decrease":
        newDifficulty = RiddleService.decreaseDifficulty(riddleId).json()['difficulty']

    return jsonify(newDifficulty=newDifficulty)


def _retrieveAllRiddles(role: str):
    riddles = None
    if role == "admin":
        riddles = RiddleService.getAllRiddles().json()
    if role == "player":
        riddles = RiddleService.getAllRiddlesOf(session['userId']).json()

    # Storing only riddle id's
    riddle_ids = [riddle['riddleId'] for riddle in riddles]

    return riddle_ids
