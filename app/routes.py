"""Where Milwaukee Crime Watch routes live"""

from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import UserInput
from crime_score_api import generate_stats


@app.route('/', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    stats = [] # show no results upon visiting page
    if form.validate_on_submit():
        zip_ = form.zip_code.data.strip()
        time_sl = form.time.data
        stats, vis_data = generate_stats(zip_, time_sl)
        g_title = f"Past 5 Years Crime score during time slot of {time_sl}"
        return render_template('user_input.html', form=form, scores=stats, values=vis_data[1], labels=vis_data[0], graph_title=g_title)
    
    return render_template('user_input.html', form=form, scores=stats)
