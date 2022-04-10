from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    lastName = StringField('Last Name', validators=[InputRequired()])
    firstName = StringField('First Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[InputRequired()])