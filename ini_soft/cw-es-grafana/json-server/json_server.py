# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def health_check():
    return 'This datasource is healhty.'

@app.route('/search', methods=['POST'])
def search():
    return jsonify(['my_series', 'another_series'])

@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": [
                [861, convert_to_time_ms(req['range']['from'])],
                [767, convert_to_time_ms(req['range']['to'])]
            ]
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
