from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    echo_str = request.args.get('echostr')
    return echo_str


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
