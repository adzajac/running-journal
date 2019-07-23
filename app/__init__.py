import os
from flask import Flask

# extensions
from flask_sqlalchemy import SQLAlchemy

# blueprints
from app.errors import error_bp



basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
def create_app(config=Config):
    app = Flask(__name__)       # __name__.split('.')[0]
    app.config.from_object(config)
    app.register_blueprint(error_bp)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
