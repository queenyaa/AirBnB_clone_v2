#!/usr/bin/python3
"""
Script to handle dynamic routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB?'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c<text>')
def c_route(text):
    # Replace underscores with spaces
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
