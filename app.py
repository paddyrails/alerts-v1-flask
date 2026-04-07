import os
from flask import Flask
from common.extensions import db, ma, migrate
from config.settings import config_map
from api import register_blueprints 

def create_app():
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config_map.get(env, config_map['default']))

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app
