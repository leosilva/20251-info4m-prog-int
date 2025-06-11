from app import app
from flask import render_template


@app.route("/")
def home():
    usuario = {
        'nome': 'Leo',
        'produtos': ['Banana', 'Abacaxi']
    }
    esta_logado = True
    return render_template("index.html", usuario = usuario, usuario_logado = esta_logado)


@app.route("/sobre")
def sobre():
    return "Página Sobre"