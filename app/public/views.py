from flask import render_template
from app.public import blueprint
from app.public.forms import LoginForm, RegisterForm
from app.extensions import db
from app.models import User


@blueprint.route('/')
def home():
    return render_template('public/index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "done"
    return render_template('public/login.html', form=form)
    
    
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return "user registered"
    return render_template('public/register.html', form=form)
