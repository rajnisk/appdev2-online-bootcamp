from controllers.auth import Register


def register_api(api):
    api.add_resource(Register, '/signup')
