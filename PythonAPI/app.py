from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import routes.cat

@app.errorhandler(400)
def handle400Error(error):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

@app.errorhandler(404)
def handle404Error(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def handle500Error(error):
    return make_response(jsonify({'error': 'Server error'}), 500)

if __name__ == '__main__':
    app.run(debug=True)