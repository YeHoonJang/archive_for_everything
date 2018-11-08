# -*- coding: utf-8 -*-
from calendar import timegm
import datetime
import _strptime
from flask import Flask, request, jsonify
app = Flask(__name__)

now = datetime.datetime.now()

@app.route('/')
def health_check():
    return 'This datasource is healhty.'

@app.route('/search', methods=['POST','GET'])
def search():
    return jsonify(['es-test'])

@app.route('/query', methods=['POST','GET'])
def query():
    req = request.get_json()
    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": [
            ]
        }
    ]

    print("req:", req['targets'],"\n")
    print("req['targets'][0]:", req['targets'][0], "\n")
    print("req['targets'][0]['target']", req['targets'][0]['target'], "\n")
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
