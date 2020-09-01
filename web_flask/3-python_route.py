#!/usr/bin/python3
"""
Time for another route
"""
from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Just print Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    """ Just print HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def some_text(text=""):
    """Adds some custom text """
    return "C " + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ Python stuff """
    text = text.replace('_', " ")
    return "Python " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)