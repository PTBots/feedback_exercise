from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    """login form"""

    username = StringField(
        "Username",
        validators = [InputRequired()]
    )
    password = PasswordField(
        "Password",
        validators = [InputRequired()]
    )

class RegisterForm(FlaskForm):
    """user registration form"""

    username = StringField(
        "Username",
        validators = [InputRequired()]
    )
    password = PasswordField(
        "Password",
        validators = [InputRequired()]
    )
    email = StringField(
        "Email",
        validators = [InputRequired()]
    )
    first_name = StringField(
        "First Name",
        validators = [InputRequired()]
    )
    last_name = StringField(
        "Last Name",
        validators = [InputRequired()]
    )

class FeedbackForm(FlaskForm):
    """feedback form"""

    title = StringField(
        "Title",
        validators = [InputRequired()]
    )

    content = StringField(
        "Content",
        validators = [InputRequired()]
    )

class DeleteForm(FlaskForm):
    """delete form -- needed -- otherwise error is thrown"""
