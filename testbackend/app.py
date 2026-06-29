from datetime import datetime
import time
from flask import Flask
from flask_restful import Resource, Api, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from extensions import db, jwt
from models import User

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = "a-very-strong-password-and-super-secret" 
api = Api(app)
db.init_app(app)
jwt.init_app(app)
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


from controllers import register_api
register_api(api)

if __name__ == '__main__':
    app.run(debug=True)