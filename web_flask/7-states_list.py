#!/usr/bin/python3
"""
Time to start making webpages with SQL yo
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Lists all the states """
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown(error):
    """ Tears it all apart """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
