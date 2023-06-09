import binascii
import os

from flask import Flask, render_template

from src.application.component.users.Ranking import rankingBP
from resources.database.database import init_db
from resources.config.properties import PORT, HOST
from src.application.component.riddles.Create import createRiddleBP
from src.application.component.riddles.Edit import editBP
from src.application.component.riddles.list import listBP
from src.application.component.game.game import gameBP
from src.application.component.users.EditUser import editUserBP
from src.application.component.users.LoginUser import loginBP
from src.application.component.users.SignUpUser import signUpBP
from src.application.component.users.UserManagement import UserManagementBP
from src.backend.riddles.api.controller.RiddleController import riddleBP
from src.backend.users.api.controller.UserController import userBP

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure and init DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'resources/database',
                                                                    'vicious_clue_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

# If change port here, should modify into blueprints
app.secret_key = binascii.hexlify(os.urandom(24))

app.register_blueprint(gameBP, url_prefix='/game')
app.register_blueprint(riddleBP, url_prefix='/riddles')
app.register_blueprint(listBP, url_prefix='/list')
app.register_blueprint(editBP, url_prefix='/edit')
app.register_blueprint(loginBP, url_prefix='/login')
app.register_blueprint(userBP, url_prefix='/users')
app.register_blueprint(signUpBP, url_prefix='/signUp')
app.register_blueprint(createRiddleBP, url_prefix='/createRiddle')
app.register_blueprint(UserManagementBP, url_prefix='/UserManagement')
app.register_blueprint(editUserBP, url_prefix='/editUser')
app.register_blueprint(rankingBP, url_prefix='/ranking')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.route('/')
def getIndex():
    return render_template('riddles/index.html')


@app.route('/rules')
def rules():
    return render_template('rules/rules.html')


if __name__ == '__main__':
    app.run(host=HOST, debug=True, port=PORT)
