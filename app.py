from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Verifique as credenciais do usuário aqui
    return f'Bem-vindo {username}'

if __name__ == '__main__':
    app.run(debug=True)