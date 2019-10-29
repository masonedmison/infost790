from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import UserInput
import datetime


@app.route('/', methods=['GET', 'POST'])
def user_input():
    predict_mock = [
        dict(name='Crime Score', score=25),
        dict(name='Median', score=25),
        dict(name='Mode', score=25)
    ]
    form = UserInput()
    if form.validate_on_submit():
        repr(type(form.time))
        return jsonify(dict(activity=form.neighborhood.data, date=form.date.data.strftime('%Y-%m-%d'),
                            time=form.time.data.strftime('%H:%M')))
    return render_template('user_input.html', form=form, scores=predict_mock)

@app.route('/output', methods=['GET'])
def output():
    pass
