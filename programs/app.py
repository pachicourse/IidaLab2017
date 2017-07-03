from flask import Flask, render_template, request
import os
import requests
import json

ROOT_ADDRESS = os.environ.get('MESH_ROOT_ADDRESS')
ROOT_PORT = os.environ.get('MESH_ROOT_PORT')

app = Flask(__name__)

def is_empty(*arg):
    #すべてに文字が入力されている時Flaseを返す
    for form_data in arg:
        if not form_data:
            return True
    return False

#ROOTにjsonを送信
def send_json(json_data):
    url = 'http://' + ROOT_ADDRESS + ':' + ROOT_PORT + '/rescue'
    r = requests.post(url, json_data, \
                      headers={'Content-Type':'application/json'})
    print(r)
    return

@app.route('/', methods=['GET', 'POST'])
def main_page():
    name = request.form.get('name')
    location = request.form.get('location')
    situation = request.form.get('situation')
    if request.method == 'POST' and not is_empty(name, location, situation):
        relay_data = json.dumps({'name':name,'location':location,
                                 'situation':situation})
        send_json(relay_data)
    return render_template('index.html')

@app.route('/rescue', methods=['POST'])
def relay_message():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return 'It is not json data.'
    print(request.json)
    send_json(json.dumps(request.json))
    return 'done'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
