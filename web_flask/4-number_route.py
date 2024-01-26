#!/usr/bin/python3
"""
Script to start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays - Hello HBNB! """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays - HBNB """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays C followed by a string """
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Displays 'Python ', followed by string"""
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Display 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
