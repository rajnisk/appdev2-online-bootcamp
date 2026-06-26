from flask_restful import Resource, request
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not username or not email or not password or not role:
            return {'msg':'all the fields are required'}

        user = User(username=username, email=email, password=generate_password_hash(password), role=role)
        db.session.add(user)
        db.session.commit()

        return {'msg':'user registered successfully!'}