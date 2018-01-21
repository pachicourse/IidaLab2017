import requests
import json
import os
import time
from contextlib import suppress

NETWORK_BROADCAST_ADDRESS = os.environ.get('NAVI_NETWORK')

class Store:
    def __init__(self, store_info, network=NETWORK_BROADCAST_ADDRESS):
        self.store_info = store_info
        self.network = network

    def broadcast_store_data(self):
        # 255.255.255.0
        # 処理的に限界(ブロードキャストできるようになったら大丈夫かも)
        for i in range(1, 255):
            # requestsでブロードキャストする方法がいまいちわからないので
            # とりあえず握りつぶす(罪深い)
            with suppress(Exception):
                url = 'http://' + self.network + str(i) + ':5000'
                print(url)
                r = requests.post(url, \
                                  json.dumps(self.store_info), \
                                  headers={'Content-Type':'application/json'},
                                  timeout=0.1)
                print(r)

if __name__ == '__main__':
    try:
        # ローカルJSONファイルの読み込み
        with open('store_data.json', 'r') as f:
            data = json.load(f)
            print(data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    store = Store(data);

    while 1:
        store.broadcast_store_data()
        time.sleep(1)

    # app.run(host="0.0.0.0", debug=False, threaded=True)
