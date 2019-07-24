from flask import Flask
from config import Config

# extensions
from app.extensions import db, login

# blueprints
from app.errors import blueprint as blueprint_errors
from app.public import blueprint as blueprint_public


    
def create_app(config=Config):
    app = Flask(__name__)       # __name__.split('.')[0]
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
    return app

def register_blueprints(app):
    app.register_blueprint(blueprint_errors)
    app.register_blueprint(blueprint_public)

def register_extensions(app):
    db.init_app(app)
    login.init_app(app)
