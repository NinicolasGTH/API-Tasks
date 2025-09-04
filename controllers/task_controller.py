from flask import request, jsonify
from models.user import db, User
from models.task import Task

class TaskController:

    @staticmethod
    def list_tasks():
        """
        Listar todas as tarefas
        ---
        tags:
          - Tasks
        summary: Retorna todas as tarefas cadastradas.
        responses:
          200:
            description: Lista de tarefas
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  title:
                    type: string
                    example: Comprar leite
                  description:
                    type: string
                    example: Ir ao supermercado
                  status:
                    type: string
                    example: pendente
                  user_id:
                    type: integer
                    example: 1
        """
        tasks = Task.query.all()
        tasks_data = [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'user_id': task.user_id,
        } for task in tasks]
        return jsonify(tasks_data), 200

    @staticmethod
    def get_taskbyid(task_id):
        """
        Retorna uma tarefa específica
        ---
        tags:
          - Tasks
        summary: Retorna uma tarefa específica
        parameters:
          - name: task_id
            in: path
            required: true
            type: integer
            description: ID da tarefa a ser retornada
        responses:
          200:
            description: Tarefa Encontrada
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                title:
                  type: string
                  example: Fazer a tabuada do 1 ao 10
                description:
                  type: string
                  example: Calcular a tabuada
                status: 
                  type: string
                  example: pendente
                user_id:
                  type: integer
                  example: 1
          404:
            description: Tarefa não encontrada
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        task_data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "user_id": task.user_id
        }
        return jsonify(task_data), 200

    @staticmethod
    def create_task():
        """
        Criar uma nova tarefa
        ---
        tags:
          - Tasks
        summary: Cria uma nova tarefa no sistema.
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - title
                - user_id
              properties:
                title:
                  type: string
                  example: Comprar leite
                description:
                  type: string
                  example: Ir ao supermercado
                user_id:
                  type: integer
                  example: 1
        responses:
          201:
            description: Tarefa criada com sucesso
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tarefa criada com sucesso
                task_id:
                  type: integer
                  example: 1
          400:
            description: Falta de campos obrigatórios
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Título e Usuário são obrigatórios
        """
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        user_id = data.get("user_id")

        if not title or not user_id:
            return jsonify({"error": "Título e Usuário são obrigatórios"}), 400

        new_task = Task(title=title, description=description, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Tarefa criada com sucesso", "task_id": new_task.id}), 201

    @staticmethod
    def update_task_status(task_id):
        """
        Atualizar status de uma tarefa
        ---
        tags:
          - Tasks
        summary: Alterna o status da tarefa entre pendente e concluído.
        parameters:
          - name: task_id
            in: path
            required: true
            type: integer
            description: ID da tarefa a ser atualizada
        responses:
          200:
            description: Status da tarefa atualizado
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Status da tarefa atualizado com sucesso
          404:
            description: Tarefa não encontrada
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        task.status = 'concluido' if task.status == 'pendente' else 'pendente'
        db.session.commit()
        return jsonify({"message": "Status da tarefa atualizado com sucesso"}), 200

    @staticmethod
    def delete_task(task_id):
        """
        Deletar uma tarefa
        ---
        tags:
          - Tasks
        summary: Remove uma tarefa do sistema pelo ID.
        parameters:
          - name: task_id
            in: path
            required: true
            type: integer
            description: ID da tarefa a ser deletada
        responses:
          200:
            description: Tarefa deletada com sucesso
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tarefa deletada com sucesso
          404:
            description: Tarefa não encontrada
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Tarefa deletada com sucesso"}), 200