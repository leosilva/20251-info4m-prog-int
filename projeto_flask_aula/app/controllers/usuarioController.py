from flask import render_template, flash
from app import db
from app.models import Usuario

class UsuarioController:
    
    def cadastrar_usuario(form):
        usuario = Usuario()
        usuario.username = form.username.data
        usuario.email = form.email.data
        usuario.password_hash = form.password.data
        
        db.session.add(usuario)
        db.session.commit()
        flash(f"O usuario {usuario.username} foi cadastrado com sucesso!")
        return render_template("index.html", usuario = usuario)