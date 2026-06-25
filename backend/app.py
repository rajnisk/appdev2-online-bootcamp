from flask import Flask
from flask_restful import Resource, Api, request
from flask_sqlalchemy import SQLAlchemy

from extensions import db, api
from models import User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
api.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

# @app.route('/')
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/name/<num>')
# def name(num):
#     return f"<p>Hello, {num}!</p>"


# =================== flask restful =================
class HelloWorld(Resource):
    def get(self):
        return {'msg': 'get'}
    
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

api.add_resource(HelloWorld, '/', '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)