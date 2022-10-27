from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def first():
    return jsonify('Test1')

@app.route('/test', methods=['GET'])
def second():
    return jsonify('Test2')

if __name__ == '__main__':
    app.run()
