from flask import render_template
from app.public import blueprint





@blueprint.route('/')
def home():
    return render_template('public/index.html')

@blueprint.route('/login')
def login():
    return render_template('public/login.html')
    
@blueprint.route('/register')
def register():
    return render_template('public/register.html')