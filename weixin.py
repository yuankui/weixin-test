from flask import Flask

app = Flask(__name__)


@app.route("/weixin")
def hello():
    return "Hello World!"
