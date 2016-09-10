# -*- coding: utf-8 -*-
from flask_restful_swagger_2 import Schema

class ErrorSchema(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }
