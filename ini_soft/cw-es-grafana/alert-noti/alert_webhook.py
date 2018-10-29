from flask import Flask, request, abort, Response
from flask_cors import CORS, cross_origin
import json
import logging
import requests
import urllib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def save_image(url):
    reqeust = urllib.request.Reqeust(url,
    headers={'Authorization':'Bearer eyJrIjoic09hcXlTY1F1eGo4OGpKb0VqdXh5OGVuVlFCWlQ1bXAiLCJuIjoidGVzdCIsImlkIjoxfQ=='})
    page = urllib.request.urlopen(request)

    with open('somefile.png','wb') as f:
        f.write(page.read())
        # f.open()

    return 'somefile.png'

@app.route('/webhook', methods=['POST, PUT'])
def webhook():
    url = r'http://13.231.223.137:3000/render/d-solo/4dgCpYbmz/ls-monit-v1-0?orgId=1&from=1540757160583&to=1540778760583&panelId=8&width=1000&height=500&tz=Asia%2FSeoul'
    file_name = save_image(url)
    f = open(file_name, 'r+')
    f.read()
    f.close()
    # f = open('somefile.png', 'r+')
    # pngdata = f.read()
    # f.close()
    # if request.method == 'POST':
    #     print(request.json)
    #     return '', 200
    # else:
    #     abort(400)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
