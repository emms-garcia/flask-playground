from flask_jwt import jwt_required, current_identity
from flask_restful import Resource
from webargs.flaskparser import use_args

from playground.models.todos import Todos
from playground.schemas.todos import TodoSchema


class TodoDetailResource(Resource):
    @jwt_required()
    def get(self, todo_id):
        user = Todos.query.filter_by(
            id=todo_id,
            user_id=current_identity.id,
        ).first()
        if user:
            return TodoSchema().dump(user)
        return {'message': 'Todo not found'}, 404


class TodoListResource(Resource):
    @jwt_required()
    def get(self):
        return TodoSchema(many=True).dump(
            Todos.query.filter_by(user_id=current_identity.id).all()
        )

    @jwt_required()
    @use_args(TodoSchema())
    def post(self, payload):
        todo = Todos(user_id=current_identity.id, **payload)
        return TodoSchema().dump(todo.create())
