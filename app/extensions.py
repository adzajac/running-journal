from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login.init_app(app)