from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "OK"

if __name__ == "__main__":
    app.run(host="192.168.10.135", port=5000, debug=True, threaded=True)
