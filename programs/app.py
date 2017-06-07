from flask import Flask, render_template, request
import os
import requests
import json

ROOT_ADDRESS = os.environ.get('ROOT_ADDRESS')
ROOT_PORT = os.environ.get('ROOT_PORT')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/resque', methods=['POST'])
def relay_message():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return 'It is not json data.'
    print(request.json)
    print(request.json['message'])
    url = 'http://' + ROOT_ADDRESS + ':' + ROOT_PORT + '/resque'
    r = requests.post(url, json.dumps(request.json), \
                      headers={'Content-Type':'application/json'})
    print(r)
    return 'done'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, threaded=True)
