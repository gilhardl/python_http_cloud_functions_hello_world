import flask

from functions import main


app = flask.Flask(__name__)


@app.route("/")
def index():
    return main.hello_world(flask.request)

@app.route("/hello")
def hello():
    return main.hello_name(flask.request)

@app.route("/powered-by")
def powered_by():
    return main.python_powered(flask.request)