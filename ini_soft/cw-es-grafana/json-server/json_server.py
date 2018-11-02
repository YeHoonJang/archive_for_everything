# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def health_check():
    return 'This datasource is healhty.'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
