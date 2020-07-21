from flask import Flask
from .extensions import db
from .routes import short
from .commands import create_tables

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(short)
    db.init_app(app)
    app.cli.add_command(create_tables)
    return app
