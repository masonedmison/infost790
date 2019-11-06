from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import required
from wtforms.fields.html5 import DateField, TimeField


# add time slots! 
class UserInput(FlaskForm):
    address = StringField('Address')
    zip_code = StringField('Zip Code', validators=[required()])
    time = SelectField('Time',validators=[required()], choices=[('12pm - 8am','12pm - 8am'),('8am - 4pm', '8am - 4pm'),('4pm -12pm', '4pm -12pm')])
    submit = SubmitField('Submit')



