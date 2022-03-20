from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropForm(FlaskForm):
    title = StringField('Property Title',validators=[DataRequired()])
    description = TextAreaField("Description",validators=[DataRequired()])
    rooms = StringField('No. of Rooms',validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])    
    propType = SelectField(u'Property Type',choices=[("House","House"),("Apartment","Apartment")])
    
    photo = FileField("Photo"
    ,validators=[
        FileRequired(),
        FileAllowed(["jpg","png"],"Images only!")
        ])