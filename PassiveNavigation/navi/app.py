import json
from flask import Flask, request

app = Flask(__name__)

class Navi:
    def __init__(self, needs_data):
        self.needs_data = needs_data

@app.route('/')
def recieve_store_data(methods=['GET','POST']):
    if reqest.method == 'POST':
        store_name = request.json['name']
        store_type = request.json['type']
        store_keyword = request.json['keywords']

    if request.method == 'GET':

if __name__ == '__main__':
    try:
        # ローカルJSONファイルの読み込み
        with open('navi_data.json', 'r') as f:
            data = json.load(f)
            print(data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    navi = Navi(data);
    app.run(host="0.0.0.0", debug=False, threaded=True)
