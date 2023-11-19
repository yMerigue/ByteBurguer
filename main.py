from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///byteburguer.db'

#database = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/cadastrocliente')
def cadastrocliente():
    return render_template('cadastrocliente.html')
if __name__ == '__main__':
    app.run(debug=True)

