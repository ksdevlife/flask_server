from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from root import db, ma, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128), unique=True)
    pw_hash = db.Column(db.String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task