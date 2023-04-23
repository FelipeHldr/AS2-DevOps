from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html')

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
