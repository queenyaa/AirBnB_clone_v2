#!/usr/bin/python3
"""
Script to start Flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display HTML page
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
