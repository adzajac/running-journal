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
    runs = current_user.runs.order_by(Run.timestamp.desc()).limit(60).all()
    injuries = current_user.injuries.order_by(Injury.timestamp.desc()).limit(60).all()
    return render_template('main/index.html', runs=runs, injuries=injuries)


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
        flash("run added")
        return redirect(url_for('main.index'))
    return render_template('main/add_run.html', form=form)


@blueprint.route('/edit_run/<run_id>')
@login_required
def edit_run(run_id):
    return 'editing run: ' + run_id


@blueprint.route('/delete_run/<run_id>')
@login_required
def delete_run(run_id):
    return 'deleting run: ' + run_id


@blueprint.route('/runs')
@login_required
def runs():
    runs = current_user.runs.order_by(Run.timestamp.desc()).all()
    return render_template('main/runs.html', runs=runs)


@blueprint.route('/add_post', methods=['POST', 'GET'])
@login_required
def add_post():
    return 'adding a post'


@blueprint.route('/add_injury', methods=['POST', 'GET'])
@login_required
def add_injury():
    form = AddInjuryForm()
    if form.validate_on_submit():
        injury = Injury(user_id=current_user.id, text=form.title.data, description=form.description.data, timestamp=form.timestamp.data)
        db.session.add(injury)
        db.session.commit()
        flash("injury added")
        return redirect(url_for('main.index'))
    return render_template('main/add_injury.html', form=form)


@blueprint.route('/edit_injury/<injury_id>')
@login_required
def edit_injury(injury_id):
    return 'editing injury: ' + injury_id


@blueprint.route('/delete_injury/<injury_id>')
@login_required
def delete_injury(injury_id):
    return 'deleting injury: ' + injury_id


@blueprint.route('/injuries')
@login_required
def injuries():
    injuries = current_user.injuries.order_by(Injury.timestamp.desc()).all()
    return render_template('main/injuries.html', injuries=injuries)
    