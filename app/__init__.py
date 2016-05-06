#coding:utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    from .main import main
    db.init_app(app)
    app.register_blueprint(main)
    return app