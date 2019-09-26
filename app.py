from flask import render_template
from root import app, api
from root.apis import TasksAPI, TaskAPI

api.add_resource(TasksAPI, '/tasks')
api.add_resource(TaskAPI, '/tasks/<id>')

from root.users.views import users
app.register_blueprint(users)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()