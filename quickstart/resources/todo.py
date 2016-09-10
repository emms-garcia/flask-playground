# -*- coding: utf-8 -*-
from flask import request
from flask_restful import HTTPException
from flask_restful_swagger_2 import Resource, swagger

from quickstart.docs.todo import DOCS
from quickstart.schemas.error import ErrorSchema
from quickstart.schemas.todo import TodoSchema

TODO_LIST = [TodoSchema(id=1, description='Work work work')]


class TodoNotFoundException(HTTPException):
    pass


class TodoResource(Resource):
    @swagger.doc({
        'tags': ['todo'],
        'description': 'Returns all todo items',
        'parameters': [
            {
                'name': 'name',
                'description': 'Name to filter by',
                'type': 'string',
                'in': 'query'
            }
        ],
        'responses': {
            '200': {
                'description': 'List of todo items',
                'schema': TodoSchema,
                'examples': {
                    'application/json': [
                        {
                            'id': 1,
                            'description': 'Something to Do.'
                        }
                    ]
                }
            }
        }
    })
    def get(self):
        return map(lambda todo: TodoSchema(**todo), TODO_LIST), 200

    @swagger.doc({
        'tags': ['todo'],
        'description': 'Adds a todo',
        'parameters': [
            {
                'name': 'body',
                'description': 'Request body',
                'in': 'body',
                'schema': TodoSchema,
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': 'Created todo',
                'schema': TodoSchema,
                'headers': {
                    'Location': {
                        'type': 'string',
                        'description': 'Location of the new item'
                    }
                },
                'examples': {
                    'application/json': {
                        'id': 1
                    }
                }
            }
        }
    })
    def post(self):
        try:
            data = TodoSchema(**request.get_json())
        except ValueError as e:
            return ErrorSchema(**{'message': e.args[0]}), 400

        data['id'] = len(TODO_LIST) + 1
        TODO_LIST.append(data)
        return data, 201


class TodoDetailResource(Resource):
    @swagger.doc({
        'tags': ['todo'],
        'description': 'Returns a todo object',
        'parameters': [
            {
                'name': 'todo_id',
                'description': 'Todo identifier',
                'in': 'path',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'Todo object',
                'schema': TodoSchema,
                'examples': {
                    'application/json': {
                        'id': 1,
                        'description': 'Work it harder.'
                    }
                }
            }
        }
    })
    def get(self, todo_id):
        todo = next((t for t in TODO_LIST if t['id'] == todo_id), None)
        if not todo:
            raise TodoNotFoundException
        return TodoSchema(**todo), 200
