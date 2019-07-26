from datetime import datetime
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.main import blueprint
from app.main.forms import AddRunForm, AddInjuryForm
from app.extensions import db, login
from app.models import User, Run, Injury



@blueprint.route('/main')
@login_required
def index():
    return render_template('main/index.html')


@blueprint.route('/profile')
@login_required
def profile():
    return 'user profile page'


@blueprint.route('/edit_profile')
@login_required
def edit_profile():
    return 'edit user profile page'
    
    
@blueprint.route('/user/<username>')
@login_required
def user(username):
    return 'view profile page of: ' + username


@blueprint.route('/add_run', methods=['POST', 'GET'])
@login_required
def add_run():
    form = AddRunForm()
    if form.validate_on_submit():
        duration = int(form.duration_h.data)*360 + int(form.duration_m.data)*60 + int(form.duration_s.data)
        timestamp = form.timestamp.data
        run = Run(user_id=current_user.id, distances=int(form.distance.data), times=str(duration), timestamp=timestamp)
        db.session.add(run)
        db.session.commit()
        return 'ok'
    return render_template('main/add_run.html', form=form)


@blueprint.route('/add_post', methods=['POST', 'GET'])
@login_required
def add_post():
    return 'adding a post'


@blueprint.route('/add_injury', methods=['POST', 'GET'])
@login_required
def add_injury():
    form = AddInjuryForm()
    if form.validate_on_submit():
        return 'ok'
    return render_template('main/add_injury.html', form=form)