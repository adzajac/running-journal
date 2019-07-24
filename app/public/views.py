from flask import render_template
from app.public import blueprint
from app.public.forms import LoginForm, RegisterForm


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
        return "done"
    return render_template('public/register.html', form=form)

























