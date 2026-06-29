from datetime import datetime

from models import Task
from extensions import db
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


class TodoResource(Resource):
    @jwt_required()
    def get(self, id=None):
        claims =get_jwt()
        if id is None:
            if claims.get('role') != 'admin':
                return {'msg': 'Access denied. Admins only.'}, 403
            Tasks = Task.query.all()
            data = []
            for Task in Tasks:
                data.append(Task.to_json())

            return {'msg': data}
        else:
            user_id = get_jwt_identity()

            task = Task.query.get(id)

            if task.assigned_to != int(user_id):
                return {'msg': 'Access denied. You are not the owner of this task.'}, 403
            return {'data': task.to_json()}

    def post(self):
        data = request.get_json()
        due_date = data.get('due_date')
        formated_due_date =datetime.strptime(due_date, "%Y-%m-%d")
        assigned_date = datetime.now()
        new_task = Task(title=data.get('title'), description=data.get('description'), status=data.get('status'), assigned_to=data.get('assigned_to'), due_date=formated_due_date, assigned_date=assigned_date)
        db.session.add(new_task)
        db.session.commit()
        return {'msg': 'new task added successfully!'}
    
    def put(self, id):
        data = request.get_json()
        due_date = data.get('due_date')
        formated_due_date =datetime.strptime(due_date, "%Y-%m-%d")
        assigned_date = datetime.now()

        task = Task.query.get(id)
        task.title = data.get('title')
        task.description = data.get('description')
        task.status = data.get('status')
        task.assigned_to = data.get('assigned_to')
        task.due_date = formated_due_date
        task.assigned_date = assigned_date

        db.session.commit()
        return {'msg': f'data updated for task with id {id}'}
    
    def delete(self, id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return {'msg': f'task with id {id} deleted!'}
