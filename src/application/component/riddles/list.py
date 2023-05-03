import requests

from src.application.service.RiddleService import RiddleService
from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray
from resources.config.properties import HOST, PORT

from flask import Blueprint, render_template, session, redirect, url_for

listBP = Blueprint('list', __name__)
enigmasByPage = 5
currentPage = 0
perPage = 5


@listBP.route('/', methods=['GET'])
@listBP.route('/<int:page>', methods=['GET'])
def getList(page=1):
    global perPage

    if session.get('userIsConnected') is None:
        return redirect(url_for('login.loginUser'))
    else:
        # Get riddles function of type of user (admin or player)
        riddles = _getRiddles(session['userRole'])
        riddlesNumber = len(riddles)

        riddlesPaginated = _paginateRiddle(riddles, perPage)
        totalPages = int((len(riddles) + perPage - 1) / perPage)

        if page > totalPages or page < 1:
            return render_template('riddles/list_empty.html')

        return render_template('riddles/list.html'
                               , riddles=riddlesPaginated[page]
                               , currentPage=page
                               , totalPages=totalPages
                               , remainingRiddle=riddlesNumber)


@listBP.route('/emptyList', methods=['GET'])
def emptyList():
    return render_template('riddles/list_empty.html')


def _getRiddles(role: str):
    riddles = None
    if role == "admin":
        riddles = RiddleService.getAllRiddles().json()
    if role == "player":
        riddles = RiddleService.getAllRiddlesOf(session['userId']).json()
    return riddles


def _paginateRiddle(riddle, maxPerPage):
    pagination = {}
    lastPage = (len(riddle) / maxPerPage) + 1
    key = 1
    indexEnigmas = 0
    while key <= lastPage:
        tempArray = []
        i = 0
        while i < 5 and indexEnigmas < len(riddle):
            tempArray.append(riddle[indexEnigmas])
            indexEnigmas += 1
            i += 1
        pagination[key] = tempArray
        key += 1
    return pagination
