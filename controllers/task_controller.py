from flask import request, jsonify
from models.user import db, User
from models.task import Task

class TaskController:
    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        tasks_data = [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'user_id': task.user_id,
        } for task in tasks]
        return jsonify(tasks_data)
    
    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form.get("title")
            description = request.form.get("description")
            user_id = request.form.get("user_id")

            if title and user_id:
                user_id = int(user_id)
                new_task = Task(title=title, description=description, user_id=user_id)
                db.session.add(new_task)
                db.session.commit()
                return jsonify({"message": "Tarefa criada com sucesso", "task_id": new_task.id}), 201
            return jsonify({"error": "Título e Usuário são obrigatórios"}), 400

        return jsonify({"error": "Método não permitido"}), 405
    
    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get(task_id)
        if task:
            task.status = 'concluido' if task.status == 'pendente' else 'pendente'
            db.session.commit()
            return jsonify({"message": "Status da tarefa atualizado com sucesso"}), 200
        return jsonify({"error": "Tarefa não encontrada"}), 404
    
    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify({"message": "Tarefa deletada com sucesso"}), 200
        return jsonify({"error": "Tarefa não encontrada"}), 404