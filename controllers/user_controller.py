from flask import request, jsonify
from models.user import db, User

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        users_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
        return jsonify(users_data)
    
    @staticmethod
    def contact():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')

            if not name or not email:
                return jsonify({"error": "Preencha todos os campos"}), 400

            if User.query.filter_by(email=email).first():
                return jsonify({"error": "Email já cadastrado"}), 409

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "Usuário cadastrado com sucesso", "user_id": new_user.id}), 201
        return jsonify({"error": "Método não permitido"}), 405