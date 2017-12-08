import requests
import json
import os


NETWORK_BROADCAST_ADDRESS = os.environ.get('NAVI_NETWORK')

class store:
    def __init__(self, store_info, network=NETWORK_BROADCAST_ADDRESS):
        self.store_info = store_info
        self.netword = network
    
    def broadcast_store_data(self):
        r = requests.post('http://' + self.network, \
                          json.dumps(self.store_info), \
                          headers={'Content-Type':'application/json'})
        print(r)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, threaded=True)
