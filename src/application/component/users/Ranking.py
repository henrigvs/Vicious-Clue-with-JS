from flask import Blueprint, render_template

rankingBP = Blueprint('ranking', __name__)


@rankingBP.route('/', methods=['GET'])
def ranking():
    return render_template('user/ranking.html')
