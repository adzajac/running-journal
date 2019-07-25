from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
from app.main import blueprint
#from app.main.forms import 
from app.extensions import db, login
from app.models import User



@blueprint.route('/main')
def index():
    return render_template('main/index.html')


#@blueprint.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        user = User.query.filter_by(username=form.username.data).first()
#        if user is not None:
#            if user.check_password(form.password.data):
#                login_user(user)
#                flash("you're now logged in")
#                return redirect(url_for('public.home'))
#    return render_template('public/login.html', form=form)
#    
#    
#@blueprint.route('/logout')
#@login_required
#def logout():
#    logout_user()
#    return redirect(url_for('public.home'))
#    
#    
#@blueprint.route('/register', methods=['GET', 'POST'])
#def register():
#    form = RegisterForm()
#    if form.validate_on_submit():
#        user = User(username=form.username.data, email=form.email.data)
#        user.set_password(form.password.data)
#        db.session.add(user)
#        db.session.commit()
#        flash("you're now registered, please log in")
#        return redirect(url_for('public.login'))
#    return render_template('public/register.html', form=form)
