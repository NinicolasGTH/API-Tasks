import os
from flask import Flask
from config import Config
from models.user import db
from controllers.user_controller import UserController
from controllers.task_controller import TaskController

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

# Rotas User
app.add_url_rule('/users', 'index', UserController.index, methods=['GET'])
app.add_url_rule('/users', 'contact', UserController.contact, methods=['POST'])

# Rotas Task
app.add_url_rule('/tasks', 'list_tasks', TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks', 'create_task', TaskController.create_task, methods=['POST'])
app.add_url_rule('/tasks/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['PUT'])
app.add_url_rule('/tasks/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)