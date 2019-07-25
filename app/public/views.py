from flask import render_template, redirect, flash, url_for
from flask_login import login_user
from app.public import blueprint
from app.public.forms import LoginForm, RegisterForm
from app.extensions import db, login
from app.models import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@blueprint.route('/')
def home():
    return render_template('public/index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.check_password(form.password.data):
                login_user(user)
                flash("you're now logged in")
                return redirect(url_for('public.home'))
    return render_template('public/login.html', form=form)
    
    
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("you're now registered, please log in")
        return redirect(url_for('public.login'))
    return render_template('public/register.html', form=form)
