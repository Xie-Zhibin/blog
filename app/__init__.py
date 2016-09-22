"""Initialize my blog."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    """Configure and register."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    from .main import main
    db.init_app(app)
    app.register_blueprint(main)
    return app
