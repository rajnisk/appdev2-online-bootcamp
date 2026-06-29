from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), default='employee')

    def to_json(self):
        return{
            "id":self.id,
            "username":self.username,
            "email": self.email,
            "role": self.role
        }
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(50), default='pending')
    due_date = db.Column(db.DateTime, nullable=False)
    assigned_date = db.Column(db.DateTime, nullable=False)

    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

