from datetime import datetime
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from app.main import blueprint
from app.main.forms import AddRunForm, AddInjuryForm, EditUserForm, EditPasswordForm
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
    return render_template('main/profile.html')


@blueprint.route('/edit_password', methods=['GET', 'POST'])
@login_required
def edit_password():
    form = EditPasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash("password updated")
        else:
            flash("incorrect password", "danger")
    return render_template('main/edit_password.html', form=form)


@blueprint.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditUserForm()
    if form.validate_on_submit():
        if current_user.check_password(form.password.data):
            email_not_in_use = User.query.filter_by(email=form.email.data).first() is None
            username_not_in_use = User.query.filter_by(username=form.username.data).first() is None 
            email_is_correct = email_not_in_use or form.email.data == current_user.email
            username_is_correct = username_not_in_use or form.username.data == current_user.username
            if email_is_correct and username_is_correct:
                user = current_user
                user.username = form.username.data
                user.email = form.email.data
                db.session.commit()
                flash("Your profile was updated.", "success")
            else:
                flash("Error: email or username already in use!", "danger")
        else:
            flash("incorrect password", "danger")
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('main/edit_profile.html', form=form)
    
    
@blueprint.route('/user/<username>')
@login_required
def user(username):
    return 'view profile page of: ' + username


@blueprint.route('/add_run', methods=['POST', 'GET'])
@login_required
def add_run():
    form = AddRunForm()
    if form.validate_on_submit():
        duration = int(form.duration_h.data)*3600 + int(form.duration_m.data)*60 + int(form.duration_s.data)
        timestamp = form.timestamp.data
        distances = '{:.0f}'.format(float(form.distance.data)*1000)
        run = Run(user_id=current_user.id, distances=distances, times=str(duration), timestamp=timestamp)
        db.session.add(run)
        db.session.commit()
        flash("run added")
        return redirect(url_for('main.index'))
    return render_template('main/add_run.html', form=form)


@blueprint.route('/edit_run/<run_id>', methods=['POST','GET'])
@login_required
def edit_run(run_id):
    run = current_user.runs.filter_by(run_id=run_id).first_or_404()
    form = AddRunForm()
    if form.validate_on_submit():
        run.distances = '{:.0f}'.format(float(form.distance.data)*1000)
        run.times = str(int(form.duration_h.data)*3600 + int(form.duration_m.data)*60 + int(form.duration_s.data))
        run.timestamp = form.timestamp.data
        db.session.commit()
        return redirect(url_for('main.runs'))
    elif request.method == 'GET':
        total_s = int(run.times)
        h=total_s//3600
        m=(total_s-h*3600)//60
        s=total_s-h*3600-m*60
        form.duration_h.data = '{:02.0f}'.format(h)
        form.duration_m.data = '{:02.0f}'.format(m)
        form.duration_s.data = '{:02.0f}'.format(s)
        form.distance.data = str(int(run.distances)/1000)
        form.timestamp.data = run.timestamp    
    return render_template('main/edit_run.html', form=form)


@blueprint.route('/delete_run/<run_id>')
@login_required
def delete_run(run_id):
    run = current_user.runs.filter_by(run_id=run_id).first_or_404()
    db.session.delete(run)
    db.session.commit()
    return redirect(url_for('main.runs'))


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


@blueprint.route('/edit_injury/<injury_id>', methods=['POST','GET'])
@login_required
def edit_injury(injury_id):
    injury = current_user.injuries.filter_by(injury_id=injury_id).first_or_404()
    form = AddInjuryForm()
    if form.validate_on_submit():
        injury.text = form.title.data
        injury.description = form.description.data
        injury.timestamp = form.timestamp.data
        db.session.commit()
        return redirect(url_for('main.injuries'))
    elif request.method == 'GET':
        form.title.data = injury.text
        form.description.data = injury.description
        form.timestamp.data = injury.timestamp    
    return render_template('main/edit_injury.html', form=form)


@blueprint.route('/delete_injury/<injury_id>')
@login_required
def delete_injury(injury_id):
    injury = current_user.injuries.filter_by(injury_id=injury_id).first_or_404()
    db.session.delete(injury)
    db.session.commit()
    return redirect(url_for('main.injuries'))


@blueprint.route('/injuries')
@login_required
def injuries():
    injuries = current_user.injuries.order_by(Injury.timestamp.desc()).all()
    return render_template('main/injuries.html', injuries=injuries)
    