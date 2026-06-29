from controllers.auth import Register, Login
from controllers.user import UserResource
from controllers.task import TodoResource


def register_api(api):
    api.add_resource(Register, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(UserResource, '/user', '/user/<int:id>')
    api.add_resource(TodoResource, '/todo', '/todo/<int:id>')