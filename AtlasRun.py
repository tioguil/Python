from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key= "Guil";

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
usuario1 = Usuario('luan', 'Luiz Antonio Marques', '1234')
usuario2 = Usuario('Nico', 'Nico Steppat', '7a1')
usuario3 = Usuario('guil', 'Guilherme', '123')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}

class Jogo(object):

    def __init__(self, nome, tipo, console):
        self.nome = nome
        self.tipo = tipo
        self.console = console

jogo1 = Jogo('Mario', 'RPG', 'SNES')
jogo2 = Jogo('Fifa', 'sport', 'ps1')
jogo3 = Jogo('Vigilante 8', 'Auto', 'ps1')
jogo4 = Jogo('Bully', 'RPG', 'ps2')
listaJogos = [jogo1, jogo2, jogo3, jogo4]

@app.route("/")
def index():
    return render_template('jogos.html', titulo ='lista de jogos', listaJogos = listaJogos);

@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        #não esta logado
        return redirect('/login')

    return render_template("addJogo.html",  titulo ='Cadastrar novo Jogo')

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    nome = request.form["nome"]
    tipo = request.form['categoria']
    console = request.form["console"]

    jogo = Jogo(nome, tipo, console)
    listaJogos.append(jogo)
    return redirect("/")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            return redirect("/")
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

app.run(debug=True)