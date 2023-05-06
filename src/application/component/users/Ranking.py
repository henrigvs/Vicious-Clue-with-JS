import requests
from flask import Blueprint, render_template

from resources.config.properties import HOST, PORT

rankingBP = Blueprint('ranking', __name__)


@rankingBP.route('/', methods=['GET'])
def ranking():
    return render_template('user/ranking.html');
