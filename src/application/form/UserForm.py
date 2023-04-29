from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp, EqualTo


class signUpForm(FlaskForm):
    firstName = StringField("Firstname", validators=[
        InputRequired(),
        Regexp(r'^[A-Za-z\s\-]+$', message="The firstname must contain only letters, spaces and '-'"),
        Length(min=1, max=25, message="The firstname must be between %(min)d and %(max)d characters!")
    ])
    lastName = StringField("LastName", validators=[
        InputRequired(),
        Regexp(r'^[A-Za-z\s\-]+$', message="The lastname must contain only letters, spaces and '-'"),
        Length(min=1, max=25, message="The lastname must be between %(min)d and %(max)d characters!")
    ])
    email = StringField("Email", validators=[
        InputRequired(),
        Email(message="Please enter a valid email address."),
        Length(min=5, max=50, message="The email must be between %(min)d and %(max)d characters!")
    ])
    confirmEmail = StringField("Confirm Email", validators=[
        InputRequired(),
        Email(message="Please enter a valid email address."),
        Length(min=5, max=50, message="The email must be between %(min)d and %(max)d characters!"),
        EqualTo('email', message="Email addresses must match.")
    ])
    password = PasswordField("Password", validators=[
        InputRequired(),
        Regexp(
            r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*\-])[A-Za-z\d!@#$%^&*\-]{8,}$',
            message="The password must contain at least one capital letter, one lowercase letter, one digit, and one special character (!@#$%^&*-)"
        ),
        Length(min=8, max=50, message="The password must be between %(min)d and %(max)d characters!")
    ])
    submit = SubmitField('Register')


class editForm(FlaskForm):
    firstName = StringField("Firstname",
                            validators=[
                                InputRequired(),
                                Regexp(r'^[A-Za-z\s\-]+$',
                                       message="The firstname must contain only letters, spaces and '-'"),
                                Length(min=1, max=25,
                                       message="The firstname must be between %(min)d and %(max)d characters!")
                            ])
    lastName = StringField("LastName",
                           validators=[
                               InputRequired(),
                               Regexp(r'^[A-Za-z\s\-]+$',
                                      message="The lastname must contain only letters, spaces and '-'"),
                               Length(min=1, max=25,
                                      message="The lastname must be between %(min)d and %(max)d characters!")
                           ])
    email = StringField("Email",
                        validators=[
                            InputRequired(),
                            Email(message="Please enter a valid email address."),
                            Length(min=5, max=50, message="The email must be between %(min)d and %(max)d characters!")
                        ])
    confirmEmail = StringField("Confirm Email",
                               validators=[
                                   InputRequired(),
                                   Email(message="Please enter a valid email address."),
                                   Length(min=5, max=50,
                                          message="The email must be between %(min)d and %(max)d characters!"),
                                   EqualTo('email', message="Email addresses must match.")
                               ])
    password = PasswordField("Password",
                             validators=[
                                 InputRequired(),
                                 Regexp(
                                     r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*\-])[A-Za-z\d!@#$%^&*\-]{8,}$',
                                     message="The password must contain at least one capital letter, one lowercase letter, one digit, and one special character (!@#$%^&*-)"
                                 ),
                                 Length(min=8, max=50,
                                        message="The password must be between %(min)d and %(max)d characters!")
                             ])
    submit = SubmitField('Edit')


class loginForm(FlaskForm):
    email = StringField("Email", validators=[
        InputRequired(),
        Email(message="Please enter a valid email address."),
        Length(min=5, max=50, message="The email must be between %(min)d and %(max)d characters!")
    ])
    password = PasswordField("Password", validators=[
        InputRequired(),
        Length(min=8, max=50, message="The password must be between %(min)d and %(max)d characters!")
    ])
