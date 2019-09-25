from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.public import blueprint
from app.public.forms import LoginForm, RegisterForm
from app.extensions import db, login
from app.models import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@blueprint.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    return render_template('public/index.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('public.index'))
    return render_template('public/login.html', form=form)
    
@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.index'))
    
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash("registration error: username taken", "danger")
            return redirect(url_for('public.register'))
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash("registration error: email already in use", "danger")
            return redirect(url_for('public.register'))
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("you're now registered, please log in")
        return redirect(url_for('public.login'))
    return render_template('public/register.html', form=form)
