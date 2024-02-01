#!/usr/bin/python3
"""
Starts a flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """ closes the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ Displays an HTML page with a list of states"""
    states_list = storage.all(State).values()
    return render_template('9-states.html', states=states_list)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays an HTML page with state information and its cities"""
    state = storage.get(State, id)
    if state:
        return render_template('9-states_cities.html', state=state)
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
