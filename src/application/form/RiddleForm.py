from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField, SelectField, widgets
from wtforms.widgets import TextInput
from wtforms.validators import InputRequired, Length, NumberRange


class ReadOnlyTextInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("readonly", True)
        return super(ReadOnlyTextInput, self).__call__(field, **kwargs)


class RiddleForm(FlaskForm):
    description = StringField("Description", validators=[
        InputRequired(),
        Length(min=5, max=200, message="The description must be between %(min)d and %(max)d characters!")
    ])
    solution = StringField("Solution", validators=[
        InputRequired(),
        Length(min=1, max=100, message="The solution must be between %(min)d and %(max)d characters!")
    ])
    clues = HiddenField("Clues")
    difficulty = IntegerField("Difficulty", validators=[
        InputRequired(),
        NumberRange(min=1, max=5, message="The difficulty must be between %(min)d and %(max)d!")
    ], widget=ReadOnlyTextInput(), default=1)
    category = SelectField("Category", validators=[InputRequired()], choices=[
        ('Animal', 'Animal'),
        ('Difficult', 'Difficult'),
        ('Easy', 'Easy'),
        ('Food', 'Food'),
        ('Funny', 'Funny'),
        ('Kids', 'Kids'),
        ('Logic', 'Logic'),
        ('Math', 'Math'),
        ('Sport', 'Sport'),
        ('Tricky', 'Tricky'),
        ('What I am', 'What I am'),
        ('Who I am', 'Who I am'),
    ])
    submit = SubmitField("Validate")



