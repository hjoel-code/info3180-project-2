"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
from app import app
from flask import render_template, request, jsonify, send_file
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")



@app.route('/api/register', methods=['POST'])
def register():
    return jsonify('Register')



@app.route('/api/auth/login', methods=['POST'])
def login():
    return jsonify('Login')



@app.route('/api/auth/logout', methods=['POST'])
def logout():
    return jsonify('logout')


@app.route('/api/cars', methods=['GET', 'POST'])
def cars():
    if (request.method == 'POST'):
        return jsonify('Add Cars')
    return jsonify('Get Cars')



@app.route('/api/cars/{car_id}', methods=['GET'])
def vehicle(car_id):
    return jsonify('Vehicle')



@app.route('/api/cars/{car_id}/favourite', methods=['POST'])
def addVehicleToFavourite():
    return jsonify('Add Vehicle to Favourite')



@app.route('/api/search', methods=['GET'])
def searchInventory():
    return jsonify('Search Inventory')


@app.route('/ap/users/{user_id}', methods=['GET'])
def getUserData(user_id):
    return jsonify('Get User')



@app.route('/api/users/{user_id}/favourites', methods=['GET'])
def getCarsUsersLike(useer_id):
    return jsonify('Get Cars user likes')








###
# The functions below should be applicable to all Flask apps.
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
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")