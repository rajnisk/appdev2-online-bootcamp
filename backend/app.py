from datetime import datetime
import time
from flask import Flask
from flask_restful import Resource, Api, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from extensions import db
from models import User

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
api = Api(app)
db.init_app(app)
# api.init_app(app)

with app.app_context():
    # db.drop_all()
    time.sleep(5)
    db.create_all()

# @app.route('/')
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/name/<num>')
# def name(num):
#     return f"<p>Hello, {num}!</p>"


# =================== flask restful =================
class UserResource(Resource):
    def get(self, id=None):
        if id is None:
            users = User.query.all()
            data = []
            for user in users:
                # data.append({'id': user.id, 'username':user.username, 'email':user.email})
                data.append(user.to_json())

            return {'msg': data}
        else:
            return {'msg': f'get user with id {id}'}

    def post(self):
        data = request.get_json()
        new_user = User(username=data.get('username'), email=data.get('email'))
        db.session.add(new_user)
        db.session.commit()
        return {'msg': 'new user added successfully!'}
    
    def put(self, id):
        data = request.get_json()
        user = User.query.get(id)
        user.username = data.get('username')
        user.email = data.get('email')
        db.session.commit()
        return {'msg': f'data updated for user with id {id}'}
    
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {'msg': 'user with id {id} deleted!'}
    

class TodoResource(Resource):
    def get(self):
        return {"msg":"todo app"}

from controllers import register_api
register_api(api)

api.add_resource(UserResource, '/user', '/user/<int:id>')
api.add_resource(TodoResource, '/todo')

if __name__ == '__main__':
    app.run(debug=True)