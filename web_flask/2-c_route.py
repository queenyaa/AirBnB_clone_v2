#!/usr/bin/python3
"""
Script to handle dynamic routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns - Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return 'HBNB'


@app.route('/c', strict_slashes=False)
def c_404():
    response = make_response("""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>""", 404)
    return response


@app.route('/c<text>', strict_slashes=False)
def c_route(text):
    """ Replace underscores with spaces"""
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
