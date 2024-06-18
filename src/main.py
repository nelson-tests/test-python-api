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
        'rightNow': datetime.datetime.now(datetime.timezone.utc),
        'data': [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
            {'name': 'Charlie', 'age': 35},
            {'name': 'David', 'age': 40},
            {'name': 'Eve', 'age': 45},
            {'name': 'Frank', 'age': 50},
            {'name': 'Grace', 'age': 55},
            {'name': 'Heidi', 'age': 60},
            {'name': 'Ivan', 'age': 65},
            {'name': 'Judy', 'age': 70},
            {'name': 'Kevin', 'age': 75},
            {'name': 'Linda', 'age': 80},
            {'name': 'Michael', 'age': 85}
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
