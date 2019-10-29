from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import required
from wtforms.fields.html5 import DateField, TimeField


class UserInput(FlaskForm):
    address = StringField('Address', validators=[required()])
    zip_code = StringField('Zip Code', validators=[required()])
    date = DateField('Date', format='%Y-%m-%d')
    time = TimeField('Time of Day', format='%H:%M')
    submit = SubmitField('Submit')



