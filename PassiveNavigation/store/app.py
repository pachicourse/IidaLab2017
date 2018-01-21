import requests
import json
import os
import time


NETWORK_BROADCAST_ADDRESS = os.environ.get('NAVI_NETWORK')

class Store:
    def __init__(self, store_info, network=NETWORK_BROADCAST_ADDRESS):
        self.store_info = store_info
        self.network = network

    def broadcast_store_data(self):
        r = requests.post('http://' + self.network, \
                          json.dumps(self.store_info), \
                          headers={'Content-Type':'application/json'})
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
