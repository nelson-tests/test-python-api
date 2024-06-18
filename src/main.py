import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/api', methods=['GET'])
def get_data():
    response = {
        'message': 'Hello, Python API!',
        'rightNow': datetime.datetime.now(datetime.timezone.utc)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
