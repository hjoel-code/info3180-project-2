"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from functools import wraps
import jwt
from app import app, db

from flask import request, jsonify, send_file, send_from_directory
import os

from app.forms import LoginForm, NewVehicleForm, RegisterForm
from app.models import Users, Cars, Favourites

from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from flask_wtf.csrf import generate_csrf

def getToken(payload):
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def getPayload(token):
    return jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

def to_dict(obj):
    dict_ = dict(obj.__dict__)
    dict_.pop('_sa_instance_state')
    return dict_

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
            
        if not token:
            return { 'message': 'Token is required', 'data': None, 'error': 'Unauthorized' }, 401
        
        
        try:
            
            data = getPayload(token)
            current_user = Users.query.filter_by(id = data['id']).first()
            
            if not current_user:
                return { 'message': 'Invalid Token', 'data': None, 'error': 'Unauthorized' }, 401
            
            
            
        except Exception as e:
            return { 'message': 'Something went wrong', 'data': None, 'error': str(e) }, 500
        
        
        return f(current_user, *args, **kwargs)
    
    
    return decorated

###
# Routing for your application.
###



@app.route('/')
def index():
    return send_file(os.path.join('../dist/', 'index.html'))



@app.route('/api/register', methods=['POST'])
def register():
    
    data = request.form.copy()
    data.update(request.files)
    form = RegisterForm(data)
    
    if (form.validate_on_submit()):
        try:
            fullname, username, password, email, location, bio = form.fullname.data, form.username.data, form.password.data, form.email.data, form.location.data, form.bio.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config.get('UPLOAD_FOLDER'), filename))
            
            
            user = Users(fullname, username, password, email, location, bio, filename)
        
       
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({ 'errors': ['User Already Exist'] })
        
        
        return jsonify({
            'success': 'New User Registered'
        })
        
    return jsonify({
        'errors': form_errors(form)
    })



@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.form.copy()
    form = LoginForm(data)
    
    if form.validate_on_submit():
        
        username, password = form.username.data, form.password.data
        user = Users.query.filter_by(username=username).first()
        
        if not user: return jsonify({ 'errors': ["User Doesn't Exist"] })
        if not check_password_hash(user.password, password): return jsonify({ 'errors': ['Incorrect Password'] })
        
        token = getToken({'fullname': user.fullName, 'photo': user.photo, 'location': user.location, 'username': user.username, 'id': user.id })
        
        return jsonify({'success': 'User Logged In', 'token': token, 'user': user.id })
    
    return jsonify({ 'errors': form_errors(form) })


@app.route('/api/auth/logout', methods=['POST'])
@auth_required
def logout(current_user):
    return jsonify({ 'message': 'User Logged Out' })


@app.route('/api/cars', methods=['POST'])
@auth_required
def cars(current_user):
    data = request.form.copy()
    data.update(request.files)
    form = NewVehicleForm(data)
    if (form.validate_on_submit()):
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        vehicle = Cars(
            description=form.description.data, make=form.make.data, model=form.model.data ,
            colour=form.colour.data ,year=form.year.data ,transmission= form.trans.data ,car_type=form.car_type.data,
            price=format(float(form.price.data), '.2f'), photo=filename, user_id=current_user.id
        )
        
        db.session.add(vehicle)
        db.session.commit()
        
        return jsonify({'success': 'Car was added successfully!'})
    
    return jsonify({'errors': form_errors(form)})



@app.route('/api/cars', methods=['GET'])
@auth_required
def getCars(current_user):
    cars = [ to_dict(car) for car in Cars.query.all() ]
    return jsonify({ 'cars': cars })


@app.route('/api/cars/<car_id>', methods=['GET'])
def vehicle(car_id):
    car = Cars.query.filter_by(id=car_id).first()
    
    if car:
        car = to_dict(car)
        return jsonify(car)
    
    return jsonify({ 'error' : "Doesn't Exist" })


@app.route('/api/cars/<car_id>/favourite', methods=['GET'])
@auth_required
def addVehicleToFavourite(current_user, car_id):
    favourite = Favourites.query.filter_by( user_id = current_user.id, car_id = car_id ).first()
    if favourite:
        db.session.delete(favourite)
        db.session.commit()
        
        return jsonify({ 'state' : 'removed' })

    data = Favourites(car_id, current_user.id)
    db.session.add(data)
    db.session.commit()
    
    return jsonify({ 'state' : 'added' })




@app.route('/api/search', methods=['GET'])
def searchInventory():
    make = request.args.get('make', None)
    model = request.args.get('model', None)
    
    cars = None
    if make and model:
        cars = Cars.query.filter_by(make = make, model= model).all()
    elif make:
        cars = Cars.query.filter_by(make = make).all()
    elif model:
        cars = Cars.query.filter_by(model= model).all()
    
    
    if cars:
        return jsonify({ 'cars' : [ to_dict(car) for car in cars ] })
    return jsonify({ 'message' : 'No Params' })


@app.route('/api/users/<user_id>', methods=['GET'])
@auth_required
def getUserData(current_user, user_id):
    cur_user = Users.query.filter_by(id=user_id).first()
    if cur_user != None:
        data = {
            'id' : cur_user.id,
            'fullName': cur_user.fullName,
            'username':cur_user.username, 
            'password':cur_user.password, 
            'email':cur_user.email, 
            'location':cur_user.location, 
            'biography':cur_user.biography, 
            'photo':cur_user.photo, 
            'date_joined':cur_user.date_joined
        }
        return jsonify(data)

    else:
        data ={'message':'This does not exist within our records. Please try again.'}
        return jsonify(data)


@app.route('/api/users/<user_id>/favourites', methods=['GET'])
@auth_required
def getCarsUsersLike(current_user, user_id):
    data = []
    fave_cars = Favourites.query.filter_by(user_id=user_id).all()
    if fave_cars:
        for fave_car in fave_cars:
            
            car_id = fave_car.car_id
            car_details= Cars.query.filter_by(id = car_id).first()
            data.append(to_dict(car_details))
            
        return jsonify({ 'cars' : data })
    
    
    return jsonify({ 'cars' : [] })
    
        


@app.route('/api/csrf-token', methods=['GET']) 
def get_csrf():
    return jsonify({ 'csrf_token': generate_csrf() })



@app.route('/api/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return send_file(os.path.join('../dist/', 'index.html'))


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")