# -*- coding: utf-8 -*-
from flask import request
from flask_restful import abort, HTTPException
from flask_restful_swagger_2 import Resource, swagger

from quickstart.schemas.todo import TodoSchema

TODO_LIST = [TodoSchema(id=1, description='Something To Do.')]


class TodoResource(Resource):
    @swagger.doc({
        'tags': ['todo'],
        'description': 'Returns all todo items.',
        'parameters': [
            {
                'name': 'query',
                'description': 'Text to filter todo items by.',
                'type': 'string',
                'in': 'query'
            }
        ],
        'responses': {
            '200': {
                'description': 'List of todo items.',
                'schema': TodoSchema,
                'examples': {
                    'application/json': [
                        {
                            'id': 1,
                            'description': 'Something To Do.'
                        }
                    ]
                }
            }
        }
    })
    def get(self, _parser):
        args = _parser.parse_args()
        filtered_todos = filter(
            lambda todo: args['query'] in todo['description'],
            TODO_LIST
        ) if args.get('query') else TODO_LIST
        return map(lambda todo: TodoSchema(**todo), filtered_todos), 200

    @swagger.doc({
        'tags': ['todo'],
        'description': 'Adds a new todo item.',
        'parameters': [
            {
                'name': 'body',
                'description': 'Request body.',
                'in': 'body',
                'schema': TodoSchema,
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': 'Created todo item.',
                'schema': TodoSchema,
                'headers': {
                    'Location': {
                        'type': 'string',
                        'description': 'Location of the new todo item resource.'
                    }
                },
                'examples': {
                    'application/json': {
                        'id': 1,
                        'description': 'Something To Do.'
                    }
                }
            }
        }
    })
    def post(self):
        try:
            data = TodoSchema(**request.get_json())
        except ValueError as e:
            abort(400, description=e.args[0])
        data['id'] = len(TODO_LIST) + 1
        TODO_LIST.append(data)
        return data, 201, {'Location': '{}/{}'.format(request.path, data['id'])}


class TodoDetailResource(Resource):
    @swagger.doc({
        'tags': ['todo'],
        'description': 'Returns a todo item.',
        'parameters': [
            {
                'name': 'todo_id',
                'description': 'Todo identifier.',
                'in': 'path',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'Todo item.',
                'schema': TodoSchema,
                'examples': {
                    'application/json': {
                        'id': 1,
                        'description': 'Something To Do.'
                    }
                }
            }
        }
    })
    def get(self, todo_id):
        todo = next((t for t in TODO_LIST if t['id'] == todo_id), None)
        if not todo:
            abort(404, description='Todo item not found.')
        return TodoSchema(**todo), 200
