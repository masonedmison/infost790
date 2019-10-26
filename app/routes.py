from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import UserInput
import datetime


# {{prediction[0]['name']}}</td>
#                   <td class="column2">{{ (100 * prediction[0]['prob']) | round}}%</td>

predict_mock = [
    dict(name='Mean', prob=.50),
    dict(name='Median', prob=.50),
    dict(name='Mode', prob=2)
]

@app.route('/', methods=['GET', 'POST'])
def user_input():
    predict_mock = [
        dict(name='Mean', prob=.50),
        dict(name='Median', prob=.50),
        dict(name='Mode', prob=2)
    ]
    form = UserInput()
    if form.validate_on_submit():
        repr(type(form.time))
        return jsonify(dict(activity=form.neighborhood.data, date=form.date.data.strftime('%Y-%m-%d'),
                            time=form.time.data.strftime('%H:%M')))
    return render_template('user_input.html', form=form, prediction=predict_mock)

@app.route('/output', methods=['GET'])
def output():
    pass
