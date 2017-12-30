import json
# import wiringpi as wp
from flask import Flask, request

#適当 あとで決める
LED_PIN = 21
app = Flask(__name__)

class Navi:
    def __init__(self, needs_data):
        self.needs_data = needs_data

    def check_needs(self, posted_data):
        return

@app.route('/', methods=['GET', 'POST'])
def recieve_store_data():
    if request.method == 'POST':
        posted_data = request.json
        store_name = request.json['name']
        store_type = request.json['type']
        store_keyword = request.json['keywords']

        print(navi.needs_data)
        print(posted_data)
        # navi.check_needs
        return 'hello'

    if request.method == 'GET':
        return

if __name__ == '__main__':
    # wp.wiringPiSetupGpio()
    # # LED_PINを出力用にセット
    # wp.pinMode(LED_PIN, 1)

    try:
        # ローカルJSONファイルの読み込み
        with open('navi_data.json', 'r') as f:
            data = json.load(f)
            print(data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    navi = Navi(data);
    app.run(host="0.0.0.0", debug=False, threaded=True)
