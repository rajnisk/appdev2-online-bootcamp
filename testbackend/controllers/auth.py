from sqlalchemy import or_

from flask_restful import Resource, request
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not username or not email or not password or not role:
            return {'msg':'all the fields are required'}

        user = User.query.filter(or_(User.email == email, User.username == username)).first()

        if user:
            return {'msg':'user with this email or username already exists'}

        user = User(username=username, email=email, password=generate_password_hash(password), role=role)
        db.session.add(user)
        db.session.commit()

        return {'msg':'user registered successfully!'}

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return {"msg":"no such user"}
        
        if not check_password_hash(user.password, password):
            return {"msg":"invalid password"}
        
        token = create_access_token(identity=str(user.id), additional_claims=user.to_json())
        return {"msg":"login successful", "token":token}