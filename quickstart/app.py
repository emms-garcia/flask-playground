# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

from flask import Flask
from flask_restful_swagger_2 import Api

from quickstart import config
from quickstart.resources.todo import TodoDetailResource, TodoResource

app = Flask(__name__)
app.config.update(
    config.CONFIG[os.environ.get('ENVIRONMENT', 'DEVELOPMENT')]
)

api = Api(
    app,
    api_version='0.1',
    api_spec_url='/api/swagger'
)
api.add_resource(TodoResource, '/api/todo')
api.add_resource(TodoDetailResource, '/api/todo/<int:todo_id>')
