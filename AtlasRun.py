from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key= "Guil";

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
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + 'logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

app.run(debug=True)