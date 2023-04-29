from flask import request, render_template, Blueprint, session, redirect, url_for
import requests

from resources.config.properties import HOST, PORT

UserManagementBP = Blueprint('UserManagement', __name__)


@UserManagementBP.route('/details/<playerId>', methods=['GET'])
def userDetails(playerId: str):
    # Only admin can have access to this information
    if session['userRole'] == "admin":

        # Retrieve information from users API
        response = requests.get(f"http://{HOST}:{PORT}/users/{playerId}")
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
