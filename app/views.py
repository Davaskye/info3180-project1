"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.models import PropInfo
from app.forms import PropForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property/create', methods=['GET', 'POST'])
def property():
    form = PropForm()
    if request.method == 'POST':
        
        if form.validate_on_submit(): # Validate file upload on submit
            
            title = form.title.data
            desc = form.description.data
            rooms = form.rooms.data
            bathrooms = form.bathrooms.data
            price = form.price.data
            location = form.location.data
            propType = form.propType.data

            photo = form.photo.data # Get file data and save to your uploads folder
            file_name = secure_filename(photo.filename)
            photo.save(os.path.join(app.config["UPLOAD_FOLDER"],file_name))

            prop = PropInfo(title, desc, rooms, bathrooms, price, location, propType, file_name)
            db.session.add(prop)
            db.session.commit()

            flash('Property has been saved', 'success')
        else:
            flash('Propery was not saved successfully.')
            return redirect(url_for('properties'))
    return render_template('propertyForm.html', form=form)

@app.route('/properties')
def properties():
    properties = PropInfo.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/property/<propertyid>')
def getProperty(propertyid):
    property = PropInfo.query.filter_by(id=propertyid).first()
    return render_template('property.html', property=property)

def get_uploaded_images():
    file_list = []
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            actual_file = os.path.join(file)
            file_list.append(actual_file)
    return file_list

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
