from flask import Flask, render_template, request
import os

ROOT_ADDRESS = os.environ.get('ROOT_ADDRESS')
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/resque', methods=['POST'])
def relay_message():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
    
    print(request.json)
    print(request.json['message'])
    return 'done'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, threaded=True)
