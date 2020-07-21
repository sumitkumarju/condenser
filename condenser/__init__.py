from flask import Flask
from .extensions import db
from .routes import short

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(short)
    db.init_app(app)
    return app

