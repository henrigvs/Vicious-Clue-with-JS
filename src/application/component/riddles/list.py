from src.application.service.RiddleService import RiddleService
from flask import Blueprint, render_template, session, redirect, url_for

listBP = Blueprint('list', __name__)
enigmasByPage = 5
currentPage = 0
perPage = 5


@listBP.route('/', methods=['GET'])
def getList():
    if session.get('userIsConnected') is None:
        return redirect(url_for('login.loginUser'))
    else:
        return render_template('riddles/list.html')


@listBP.route('/emptyList', methods=['GET'])
def emptyList():
    return render_template('riddles/list_empty.html')

