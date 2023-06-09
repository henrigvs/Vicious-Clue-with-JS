from flask import render_template, Blueprint, session
from src.application.service.UserService import UserService

UserManagementBP = Blueprint('UserManagement', __name__)


@UserManagementBP.route('/details/<playerId>', methods=['GET'])
def userDetails(playerId: str):
    # Only admin can have access to this information
    if session['userRole'] == "admin":

        # Retrieve information from users API
        response = UserService.getUserById(playerId)
        if response.status_code == 200:
            data = response.json()
            return render_template('user/user_details.html',
                                   playerId=data['userId'],
                                   playerFirstName=data['firstName'],
                                   playerLastName=data['lastName'],
                                   playerEmail=data['email'],
                                   playerRole=data['role']
                                   )
        # Handle case if the player doesn't exist
        else:
            data = response.json()
            return render_template('user/user_details.html',
                                   errorMessage=data['message']
                                   )
    else:
        return render_template('user/user_details.html',
                               errorMessage="Only an admin can have an access to player details")
