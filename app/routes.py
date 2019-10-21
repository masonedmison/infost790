from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import UserInput
import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    if form.validate_on_submit():
        repr(type(form.time))
        return jsonify(dict(activity=form.activity_type.data, date=form.date.data.strftime('%Y-%m-%d'),
                            time=form.time.data.strftime('%H:%M')))
    return render_template('user_input.html',title='User Input', form=form) 
