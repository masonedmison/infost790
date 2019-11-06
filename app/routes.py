"""Where Milwaukee Crime Watch routes live"""

from flask import render_template, flash, redirect, jsonify
from app import app
from crime_score_api import generate_stats
from app.forms import UserInput



@app.route('/', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    stats = [] # show no results upon visiting page
    if form.validate_on_submit():
        #score_dict = calculate_scores(form.zip_code, form.time)
        zip_ = form.zip_code.data
        stats = generate_stats(zip_) 
        return render_template('user_input.html', form=form, scores=stats)
    
    return render_template('user_input.html', form=form, scores=stats)
