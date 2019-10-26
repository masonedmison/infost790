from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.html5 import DateField, TimeField
# from wtforms_components import TimeField

class UserInput(FlaskForm):
    neighborhood = SelectField(
	'Neighborhood',choices=[('Downtown','Downtown'), ('Brady','Brady'), ('Bayview', 'Bayview'), ('Walkers Point',
                            'Walkers Point')] )
    date = DateField('Date', format='%Y-%m-%d')
    time = TimeField('Time of Day', format='%H:%M')
    submit = SubmitField('Submit')
