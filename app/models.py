# Add any model classes for Flask-SQLAlchemy here

from . import db
from werkzeug.security import generate_password_hash



class Cars(db.Model):
    __tablename__ = 'cars_table'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    make = db.Column(db.String(25), nullable=False)
    model = db.Column(db.String(25), nullable=False)
    colour = db.Column(db.String(25), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    transmission = db.Column(db.String(25), nullable=False)
    car_type = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Decimal(15, 2), nullable=False)
    photo = db.Column(db.Sting(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    
    def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, user_id):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id
        
    
class Users(db.Model):
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    # date_joined = db.Column(db.Date()) ---Check Later
    
    def __init__(self, firstName, lastName, username, password, email, location, biography, photo):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_time = None
        
    
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
  

class Favourites(db.Model):
    __tablename__ = 'favourites_table'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    
    
    def __init__(self, car_id, user_id):
        self.car_id = car_id
        self.user_id = user_id
    
    

