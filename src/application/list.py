import requests
from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray
from resources.config.properties import HOST, PORT
from src.application.static_methods.Pagination import Pagination

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

        riddlesPaginated = Pagination.paginateRiddle(riddles, perPage)
        totalPages = int((len(riddles) + perPage - 1) / perPage)

        if page > totalPages or page < 1:
            return render_template('riddles/list_empty.html')

        return render_template('riddles/list.html'
                               , riddles=riddlesPaginated[page]
                               , currentPage=page
                               , totalPages=totalPages)


def _getRiddles(role: str):
    riddlesResponse = None
    if role == "admin":
        riddlesResponse = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddles")
    elif role == "player":
        riddlesResponse = requests.get(f"http://{HOST}:{PORT}/riddles/getAllRiddlesOf/{session['userId']}")
    riddles = convertJSONToERiddlesArray(riddlesResponse.json())
    return riddles
