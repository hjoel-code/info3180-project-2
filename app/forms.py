from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, FloatField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    email = StringField('Email', name='email', validators=[InputRequired()])
    fullname = StringField('Full Name', name='fullname', validators=[InputRequired()])
    username = StringField('Username', name='username', validators=[InputRequired()])
    password = PasswordField('Password', name='password', validators=[InputRequired()])
    location = StringField('Location', name='location', validators=[InputRequired()])
    bio = TextAreaField('Biography', name= 'bio', validators=[InputRequired()])
    photo = FileField('Photo', name='photo', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
class NewVehicleForm(FlaskForm):
    
    description = TextAreaField('Description', validators=[InputRequired()])
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = IntegerField('Year', validators=[InputRequired()])
    trans = StringField('Transmission', validators=[InputRequired()])
    car_type = StringField('Body Type', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    photo = FileField('Photo', name='photo', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    
