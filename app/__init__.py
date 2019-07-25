from flask import Flask
from config import Config

# extensions (import before blueprints!)
from app.extensions import db, login, register_extensions
from app.database import init_database

# blueprints
from app.errors import blueprint as blueprint_errors
from app.public import blueprint as blueprint_public


    
def create_app(config=Config):
    app = Flask(__name__)       # __name__.split('.')[0]
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
    init_database(app)
    return app


def register_blueprints(app):
    app.register_blueprint(blueprint_errors)
    app.register_blueprint(blueprint_public)

