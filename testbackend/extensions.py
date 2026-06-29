from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, request
from flask_jwt_extended import JWTManager

api = Api()
db = SQLAlchemy()
jwt = JWTManager()