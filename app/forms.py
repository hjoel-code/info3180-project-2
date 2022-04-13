from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, FloatField, FileField
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
    
    description = TextAreaField('Description', validators=[])
    make = StringField('Make', validators=[])
    model = StringField('Model', validators=[])
    colour = StringField('Colour', validators=[])
    year = IntegerField('Year', validators=[])
    transmission = StringField('Transmission', validators=[])
    car_type = StringField('Body Type', validators=[])
    price = FloatField('Price', validators=[])
    photo = FileField('Images', validators=[])
    
