from flask_restful import Resource, reqparse
from root import db
from root.models import Task, TaskSchema


class TasksAPI(Resource):
    field_name_arr = ['description', 'completed']
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description')
        self.parser.add_argument('completed')
        super(TasksAPI, self).__init__()

    def post(self):
        args = self.parser.parse_args()
        task = Task(args['description'], args['completed'])
        db.session.add(task)
        db.session.commit()
        data = TaskSchema().dump(task)
        return data, 201 
    
    def get(self):
        tasks = Task.query.all()
        data = TaskSchema(many=True).dump(tasks)
        return data

class TaskAPI(Resource):
    field_name_arr = ['description', 'completed']
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description')
        self.parser.add_argument('completed')
        super(TaskAPI, self).__init__()

    def put(self, id):
        task = Task.query.get_or_404(id)
        args = self.parser.parse_args()
        if args[TaskAPI.field_name_arr[0]]:
            task.description = args['description']
        if args[TaskAPI.field_name_arr[1]]:
            task.completed = args['completed']
        db.session.commit()
        data = TaskSchema().dump(task)
        return data
    
    def delete(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        data = TaskSchema().dump(task)
        return data
    
    def get(self, id):
        task = Task.query.get_or_404(id)
        data = TaskSchema().dump(task)
        return data

