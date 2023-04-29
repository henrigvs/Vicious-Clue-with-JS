import requests
from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash

from src.application.form.UserForm import editForm
from src.application.users.ConnectUserInSession import ConnectUserInSession
from resources.config.properties import HOST, PORT

editUserBP = Blueprint('editUser', __name__)


@editUserBP.route('/<playerId>', methods=['GET', 'POST'])
def editUser(playerId: str):
    form = editForm()
    response = requests.get(f"http://{HOST}:{PORT}/users/{playerId}")
    data = response.json()

    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = generate_password_hash(form.password.data, "sha256")

        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "role": data['role'],
            'isConnected': data['isConnected']
        }

        # Call the user API to edit player in BP
        response = requests.put(f"http://{HOST}:{PORT}/users/edit/{playerId}",
                                json=payload)
        if response.status_code == 200:
            ConnectUserInSession.disconnectUser()
            return render_template('user/edit_confirmation.html')
        else:
            return render_template('user/edit_user.html',
                                   form=form,
                                   error=data['message'],
                                   defaultFirstName=data['firstName'],
                                   defaultLastName=data['lastName'],
                                   defaultEmail=data['email'])

    else:
        return render_template('user/edit_user.html',
                               form=form,
                               userID=playerId,
                               defaultFirstName=data['firstName'],
                               defaultLastName=data['lastName'],
                               defaultEmail=data['email'])
