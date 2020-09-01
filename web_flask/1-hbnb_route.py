#!/usr/bin/python3
"""
HBNB path
"""


from web_flask import app


@app.route('/', strict_slashes=False)
def chicken():
    """ Not a chicken. Stop asking """
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def pineapples():
    """ Not a pineapple, sadly """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
