from flask import render_template, Blueprint, session, redirect, url_for
import requests

from src.application.form.UserForm import loginForm
from src.application.users.ConnectUserInSession import ConnectUserInSession
from resources.config.properties import HOST, PORT

loginBP = Blueprint('login', __name__)


@loginBP.route('/', methods=['GET', 'POST'])
def loginUser():
    form = loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        json = {
            "email": email,
            "password": password
        }

        response = requests.put(f"http://{HOST}:{PORT}/users/login", json=json)
        if response.status_code == 200:
            data = response.json()
            ConnectUserInSession.connectUser(data)
            return render_template('user/login.html',  # Simplify that !!!
                                   userID=session['userId'],
                                   userName=session['userName'],
                                   userLastName=session['userLastName'],
                                   userEmail=session['userEmail'],
                                   userRole=session['userRole'],
                                   userConnectionStatus=session['userIsConnected'])
        else:
            data = response.json()
            errorMessage = data['message']
            return render_template('user/login.html', errorMessage=errorMessage, userConnectionStatus=False, form=form)

    else:
        userId = session.get('userId')
        userName = session.get('userName')
        userLastName = session.get('userLastName')
        userEmail = session.get('userEmail')
        userRole = session.get('userRole')
        userIsConnected = session.get('userIsConnected')

        if userId is None:
            return render_template('user/login.html', userConnectionStatus=False, form=form)
        else:
            return render_template('user/login.html',
                                   userID=userId,
                                   userName=userName,
                                   userLastName=userLastName,
                                   userEmail=userEmail,
                                   userRole=userRole,
                                   userConnectionStatus=userIsConnected)


@loginBP.route('/logout', methods=['POST'])
def logoutUser():
    userId = session.get('userId')
    ConnectUserInSession.disconnectUser()
    jsonUserId = {"userId": userId}
    requests.put(f"http://{HOST}:{PORT}/users/logout", json=jsonUserId)
    return redirect(url_for('login.loginUser'))
