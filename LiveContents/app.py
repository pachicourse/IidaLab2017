from flask import Flask, render_template, request, session, redirect, url_for
import os
from configparser import ConfigParser

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.before_request
def before_request():
    #Not login yet
    #Don't exclude static directory
    print(request.endpoint)
    if 'password' not in session and request.endpoint not in ('login', 'static'):
        return redirect(url_for('login'))

    #Already login
    return

@app.route('/login', methods=['GET', 'POST'])
def login():
    #User logged in
    if request.method == 'POST' and _is_account_valid():
        session['password'] = request.form['password']
        return redirect(url_for('index'))

    #return to login page
    return render_template('login.html')

def _is_account_valid():
    #Read user info from config.ini
    config = ConfigParser()
    config.read('./config.ini')
    password = request.form.get('password')
    if password == config['content']['password']:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
