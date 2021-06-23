import os
import flask

def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    return "Hello World!"

def hello_name(request):
    """HTTP Cloud Function with arguments.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    args = request.args

    if args and "name" in args:
        name = args["name"]
    else:
        name = "World"
    return "Hello {}!".format(flask.escape(name))

def python_powered(request):
    """HTTP Cloud Function which returns a file.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response file, a JPG image that says "Python Powered"
    """
    return flask.send_from_directory(os.getcwd(), "python_powered.jpg", mimetype="image/jpg")