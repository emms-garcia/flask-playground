from flask_restful import Api

from playground.resources.users import UserIdentityResource, UserListResource
from playground.resources.todos import TodoDetailResource, TodoListResource

api = Api()

# Todos
api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoDetailResource, '/todos/<todo_id>')

# Users
api.add_resource(UserIdentityResource, '/identity')
api.add_resource(UserListResource, '/users')
