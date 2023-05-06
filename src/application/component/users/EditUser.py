from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash

from src.application.form import UserForm
from src.application.service.UserService import UserService
from src.application.component.users.ConnectUserInSession import ConnectUserInSession

editUserBP = Blueprint('editUser', __name__)


@editUserBP.route('/<playerId>', methods=['GET', 'POST'])
def editUser(playerId: str):
    form = UserForm.editForm()
    response = UserService.getUserById(playerId)
    data = response.json()

    role = data.get('role')
    isConnected = data.get('isConnected')
    bestScore = data.get('bestScore')
    clueRequested = data.get('clueRequested')
    consecutiveSeriesOfThree = data.get('consecutiveSeriesOfThree')
    correctAnswer = data.get('correctAnswer')
    incorrectAnswer = data.get('incorrectAnswers')

    # Fetch inputs from form
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = generate_password_hash(form.password.data, "sha256")

        # Call the user API to edit player in BP
        response = UserService.editUser(playerId, firstName, lastName, email, password, role, isConnected, bestScore,
                                        clueRequested, consecutiveSeriesOfThree, correctAnswer, incorrectAnswer)

        # Handle Http response
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
