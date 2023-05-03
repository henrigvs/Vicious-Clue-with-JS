from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash
from src.application.form.UserForm import signUpForm
from src.application.service.UserService import UserService

signUpBP = Blueprint('signUp', __name__)


@signUpBP.route('/', methods=['GET', 'POST'])
def signUpUser():
    form = signUpForm()

    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = generate_password_hash(form.password.data, "sha256")

        # Call user API with JSON payload to add user in DB
        response = UserService.addUser(firstName, lastName, email, password, "player")
        data = response.json()
        if response.status_code == 201:
            return render_template('user/register_confirmation.html',
                                   userFirstName=firstName)
        else:
            return render_template('user/sign_up.html', form=form, error=data['message'])
    else:
        return render_template('user/sign_up.html', form=form)
