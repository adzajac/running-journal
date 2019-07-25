from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
from app.main import blueprint
#from app.main.forms import 
from app.extensions import db, login
from app.models import User



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


@blueprint.route('/add_run')
@login_required
def add_run():
    return 'adding a run'

@blueprint.route('/add_post')
@login_required
def add_post():
    return 'adding a post'

@blueprint.route('/add_injury')
@login_required
def add_injury():
    return 'adding an injury'