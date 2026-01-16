from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configurações do banco de dados MySQL
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        database='user_authentication',
        user='root',  # Insira seu usuário MySQL
        password='1234'  # Insira sua senha MySQL
    )

# Página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            connection.commit()
            cursor.close()
            connection.close()

            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('login'))

        except Error as e:
            flash(f'Ocorreu um erro: {e}', 'danger')

    return render_template('register.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            connection = create_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Usuário ou senha inválidos', 'danger')

            cursor.close()
            connection.close()

        except Error as e:
            flash(f'Ocorreu um erro: {e}', 'danger')

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    return 'Bem-vindo ao dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
