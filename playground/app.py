# -*- coding: utf-8 -*-
from flask import Flask

from playground.auth import jwt
from playground.config import Config
from playground.models import db
from playground.resources import api

app = Flask(__name__)
app.config.from_object(Config)

# Flask extensions
api.init_app(app)
db.init_app(app)
jwt.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
