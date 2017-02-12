from flask import Flask
import logging

from playground.auth import jwt
from playground.configs import CONFIG
from playground.models import db
from playground.resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG)

    # Disable flask_jwt logging
    logging.getLogger('flask_jwt').disabled = True

    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    return app


app = create_app()
