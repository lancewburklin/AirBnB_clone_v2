#!/usr/bin/python3
"""
Time for another route but with a number
"""
from flask import Flask, render_template
app = Flask(__name__)


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


@app.route('/number/<int:n>', strict_slashes=False)
def a_num(n):
    """ Prints if the input is a number """
    if type(n) == int:
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def post_num(n):
    """ Posts a number to a template """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
