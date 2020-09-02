#!/usr/bin/python3
"""
Here we are again, with more Flask stuff
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def chicken():
    """ More chicken stuff I guess """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def pineapples():
    """ Pineapples are cool """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cheese(text=""):
    """ No cheese for sure """
    return 'C ' + text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
