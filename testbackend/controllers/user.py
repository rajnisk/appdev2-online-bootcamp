from models import User
from extensions import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

class UserResource(Resource):
    @jwt_required()
    def get(self, id=None):
        username = get_jwt_identity()
        print(f"Authenticated user: {username}")
        jwt_claims = get_jwt()
        print(f"JWT Claims: {jwt_claims}")
        role = jwt_claims.get('role')
        print(f"User role: {role}")
        if role != 'admin':
            return {'msg': 'Access denied. Admins only.'}, 403
        if id is None:
            users = User.query.all()
            data = []
            for user in users:
                # data.append({'id': user.id, 'username':user.username, 'email':user.email})
                data.append(user.to_json())

            return {'msg': data}
        else:
            user = User.query.get(id)
            if user is None:
                return {'msg': f'User with id {id} not found'}, 404
            return {'data': user.to_json()}

    def post(self):
        data = request.get_json()
        new_user = User(username=data.get('username'), email=data.get('email'))
        db.session.add(new_user)
        db.session.commit()
        return {'msg': 'new user added successfully!'}
    
    def put(self, id):
        data = request.get_json()
        user = User.query.get(id)
        if user is None:
            return {'msg': f'User with id {id} not found'}, 404
        user.username = data.get('username')
        user.email = data.get('email')
        db.session.commit()
        return {'msg': f'data updated for user with id {id}'}
    
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {'msg': 'user with id {id} deleted!'}
