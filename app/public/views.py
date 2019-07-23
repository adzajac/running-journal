from flask import render_template
from app.public import blueprint





@blueprint.route('/')
def home():
    return 'home page this is'


@blueprint.route('/login')
def login():
    return 'please login'
    