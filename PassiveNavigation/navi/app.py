import json
# import wiringpi as wp
from flask import Flask, request, render_template

#適当 あとで決める
LED_PIN = 21
app = Flask(__name__)

class Navi:
    def __init__(self, json_data):
        self.needs_data = json_data['needs']

    def is_needed(self, posted_data):
        result = ''

        for n in self.needs_data:
            matched_type = self._check_type(n['type'], posted_data['type'])
            matched_keywords = self._check_keywords(n['keywords'], posted_data['keywords'].split(','))
            if matched_type and matched_keywords:
                result = 'マッチしました!\nタイプ：' + matched_type + '\n'
                result = result + 'キーワード：' + matched_keywords + '\n'
                result = result + '住所：' + posted_data['address']

        return result

    # 存在するならその店舗タイプを、そうでなければ空文字を返す
    def _check_type(self, navi_type, store_type):
        if navi_type == store_type:
            return navi_type
        else:
            return ''

    # 存在するならマッチしたキーワードを' 'で区切った文字列を、そうでなければ空文字を返す
    def _check_keywords(self, navi_keywords, store_keywords):
        result = ''
        for k in store_keywords:
            if k in navi_keywords:
                result = result + k + ' '

        return result


@app.route('/', methods=['GET', 'POST'])
def recieve_store_data():
    if request.method == 'POST':
        posted_data = request.json
        send_message = navi.is_needed(posted_data)
        if send_message:
            print(send_message)

        return 'hello'

    if request.method == 'GET':
        return render_template('index.html')

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
