from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange


class CreateRiddleForm(FlaskForm):
    description = StringField("Description", validators=[
        InputRequired(),
        Length(min=5, max=200, message="The description must be between %(min)d and %(max)d characters!")
    ])
    solution = StringField("Solution", validators=[
        InputRequired(),
        Length(min=1, max=100, message="The solution must be between %(min)d and %(max)d characters!")
    ])
    clue = StringField("Clue", validators=[
        InputRequired(),
        Length(min=1, max=100, message="The clue must be between %(min)d and %(max)d characters!")
    ])
    difficulty = IntegerField("Difficulty", validators=[
        InputRequired(),
        NumberRange(min=1, max=5, message="The difficulty must be between %(min)d and %(max)d!")
    ])
    submit = SubmitField("Create Riddle")
