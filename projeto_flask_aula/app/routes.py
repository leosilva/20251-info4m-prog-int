from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.forms.usuario_form import UsuarioForm
from app.controllers.authenticationController import AuthenticationController
from app.controllers.usuarioController import UsuarioController


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


@app.route("/inserir", methods=['GET', 'POST'])
def cadastrar_usuario():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        return UsuarioController.cadastrar_usuario(formulario)
    return render_template('cadastro_usuario.html', title='Cadastro de Usuario', form = formulario)