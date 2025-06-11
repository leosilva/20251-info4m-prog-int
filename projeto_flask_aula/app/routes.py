from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.controllers.authenticationController import AuthenticationController


@app.route("/")
def home():
    return render_template("index.html", usuario = None, usuario_logado = False)


@app.route("/sobre")
def sobre():
    return "Página Sobre"


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return AuthenticationController.login(formulario)
    return render_template('login.html', title='Login', form = formulario)