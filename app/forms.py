from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import required, any_of
from wtforms.fields.html5 import DateField, TimeField
from mappings import zip_populations, time_slots

# add time slots! 
class UserInput(FlaskForm):
    address = StringField('Address')
    zip_code = StringField('Zip Code', validators=[any_of(list(zip_populations.keys()), message='Please Enter a Milwaukee Zip Code.')])
    time = SelectField('Time', choices=[*time_slots])
    submit = SubmitField('Submit')
