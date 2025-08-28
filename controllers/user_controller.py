from flask import render_template, request, redirect, url_for
from models.user import db, User

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
    
    @staticmethod
    def contact():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')

            if not name or not email:
                return render_template('contact.html', error="Preencha todos os campos")

            if User.query.filter_by(email=email).first():
                return render_template('contact.html', error="Email já cadastrado")

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

        return render_template('contact.html')