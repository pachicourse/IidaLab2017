from flask import Flask, render_template

ROOT_ADDRESS = os.environ.get('ROOT_ADDRESS')
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, threaded=True)
