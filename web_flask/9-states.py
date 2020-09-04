#!/usr/bin/python3
"""
Time to start making webpages with SQL yo but now with cities
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=None):
    """ Lists all the states or State with ID """
    states = storage.all(State)
    if (id != None):
        thingy = "State." + str(id)
        new_state = states.get(thingy)
        if new_state:
            id = 1
            states = new_state
    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def teardown(error):
    """ Tears it all apart """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
