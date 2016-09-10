# -*- coding: utf-8 -*-
from flask_restful_swagger_2 import Resource, swagger

from quickstart.schemas.error import ErrorSchema
from quickstart.schemas.todo import TodoSchema

todo_list = []

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
    def get(self, _parser):
        """
        Returns all users.
        :param _parser: Query parameter parser
        """
        # swagger.doc decorator returns a query parameter parser in the special
        # '_parser' function argument if it is present
        args = _parser.parse_args()

        users = ([u for u in known_users if u['name'] == args['name']]
                 if 'name' in args else known_users)

        # Return data through schema model
        return map(lambda user: UserModel(**user), users), 200
    @swagger.doc({
        'tags': ['todo'],
        'description': 'Adds a todo',
        'parameters': [
            {
                'name': 'body',
                'description': 'Request body',
                'in': 'body',
                'schema': TodoSchema,
                'required': True,
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
        """
        Adds a todo item.
        """
        # Validate request body with schema model
        try:
            data = TodoSchema(**request.get_json())

        except ValueError as e:
            return ErrorSchema(**{'message': e.args[0]}), 400

        data['id'] = len(todo_list) + 1
        todo_list.append(data)
        return data, 201, {'Location': request.path + '/' + str(data['id'])}

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
        """
        Returns a specific todo item.
        :param todo_id: The todo item identifier.
        """
        todo = next((t for t in todo_list if t['id'] == todo_id), None)

        if todo is None:
            return ErrorSchema(**{'message': "Todo id {} not found".format(todo_id)}), 404

        # Return data through schema model
        return TodoSchema(**todo), 200
