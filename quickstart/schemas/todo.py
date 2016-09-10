# -*- coding: utf-8 -*-
from flask_restful_swagger_2 import Schema

class TodoSchema(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64',
        },
        'description': {
            'type': 'string'
        },
    }
    required = ['id', 'description']
