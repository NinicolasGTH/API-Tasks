from flask import Flask
from flasgger import Swagger
from models.user import db
from controllers.user_controller import UserController
from controllers.task_controller import TaskController

# Cria a aplicação Flask
app = Flask(__name__)
app.config.from_object('config.Config')  # ajuste conforme seu config.py

# Inicializa o banco
db.init_app(app)

# Template Swagger 2.0
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Usuários e Tarefas",
        "version": "1.0",
        "description": "Documentação da API usando Flask + Flasgger"
    }
}

# Inicializa Swagger
swagger = Swagger(app, template=swagger_template)

# Cria as tabelas do banco
with app.app_context():
    db.create_all()

# Rotas User
app.add_url_rule('/users', 'index', UserController.index, methods=['GET'])
app.add_url_rule('/users', 'contact', UserController.contact, methods=['POST'])

# Rotas Task
app.add_url_rule('/tasks', 'list_tasks', TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks/<int:task_id>', 'get_task_by_id', TaskController.get_taskbyid, methods=['GET'])
app.add_url_rule('/tasks', 'create_task', TaskController.create_task, methods=['POST'])
app.add_url_rule('/tasks/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['PUT'])
app.add_url_rule('/tasks/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True, port=5002)
