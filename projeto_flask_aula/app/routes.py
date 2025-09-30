from app import app
from flask import render_template, flash, redirect, url_for
from app.forms.login_form import LoginForm
from app.forms.usuario_form import UsuarioForm
from app.controllers.authenticationController import AuthenticationController
from app.controllers.usuarioController import UsuarioController


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return "Página Sobre"


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
            flash("Login realizado com sucessoo!", "success")
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos", "error")
    return render_template('login.html', title='Login', form = formulario)


@app.route('/logout', methods=['GET'])
def logout():
    AuthenticationController.logout()
    return redirect(url_for("home"))


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():       
        sucesso = UsuarioController.salvar(formulario)
        if sucesso:
            flash("Usuário cadastrado com sucesso!", category='success')
            return redirect(url_for('login'))
        else:
            flash("Erro ao cadastrar o novo usuário.", category='error')
            return render_template("cadastro.html", form = formulario)
    return render_template("cadastro.html", form = formulario)


@app.route('/listar', methods=['GET'])
def listar():
    lista_usuarios = UsuarioController.listar_usuarios()
    return render_template("listar.html", usuarios = lista_usuarios)


@app.route('/listar_filtro', methods=['GET'])
def listar_com_filtro():
    username = 'leosilva'
    usuario = UsuarioController.buscar_por_username(username)
    print(usuario.id, usuario.username, usuario.email)    
    return render_template("index.html")


@app.route('/atualizar/<int:id>', methods=['GET'])
def atualizar(id):
    form = UsuarioForm()
    form.username = 'atualizei_de_novo'
    UsuarioController.atualizar_usuario(id, form)
    return render_template("index.html")


@app.route('/remover/<int:id>', methods=['GET'])
def remover(id):
    UsuarioController.remover_usuario(id)
    return render_template("index.html")