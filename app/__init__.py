
from flask import Flask
from config import Config

# extensions
from flask_sqlalchemy import SQLAlchemy

# blueprints
from app.errors import error_bp


db = SQLAlchemy()

    
def create_app(config=Config):
    app = Flask(__name__)       # __name__.split('.')[0]
    app.config.from_object(config)
    app.register_blueprint(error_bp)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
