#!/usr/bin/python3
"""
First Flask script
"""


from web_flask import app


@app.route('/', strict_slashes=False)
def chicken():
    """ This is not a chicken """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
