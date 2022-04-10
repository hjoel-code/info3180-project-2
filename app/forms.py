from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    lastName = StringField('Last Name', validators=[InputRequired()])
    firstName = StringField('First Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[InputRequired()])
    location = SelectField('Location', choices = [], validators=[InputRequired()])
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
class NewVehicleForm(FlaskForm):
    pass