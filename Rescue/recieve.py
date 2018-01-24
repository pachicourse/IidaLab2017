# WANと接続されている端末用プログラム

from flask import Flask, render_template, request
from email.mime.text import MIMEText
import os
import requests
import json
import smtplib
import datetime

GMAIL_ADDRESS = os.environ.get('GMAIL_ADDRESS')
GMAIL_PASS = os.environ.get('GMAIL_PASS')

app = Flask(__name__)

@app.route('/rescue', methods=['POST'])
def posted_json():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return 'It is not json data.'
    # print(request.json)
    send_email_self(request.json, GMAIL_ADDRESS, GMAIL_PASS)
    return 'OK'

def send_email_self(json, address, password):
    jp='iso-2022-jp'

    raw_msg = ''

    for key in json:
        raw_msg = raw_msg + key + '\n' + json[key] + '\n\n'

    msg = MIMEText(raw_msg, 'plain', jp,)
    fromaddr = address
    toaddr = address

    # Subject指定の時に使う
    d = datetime.datetime.now()
    date = d.strftime("%Y-%m-%d %H:%M")

    msg['Subject'] = date + ' 救援要請'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    try:
        # gmailを利用して送信
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(address, password)
        server.send_message(msg)
        print('Successfully sent email')
        server.close()
        return 'Successfully sent email'
    except Exception:
        print('Error: unable to send email')
        import traceback
        traceback.print_exc()
        return 'Error: unable to send email'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
