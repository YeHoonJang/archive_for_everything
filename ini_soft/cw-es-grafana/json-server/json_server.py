# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def health_check():
    return 'This datasource is healhty.'

@app.route('/search', methods=['POST'])
def search():
    return jsonify(['my_series', 'another_series'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
