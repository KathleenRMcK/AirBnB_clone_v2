#!/usr/bin/python3
"""
Start Flask web app and display "Hello HBNB!"
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_text():
    """
    Returns "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns "C" followed by val of text w space replace
    """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Returns "Python" followed by val of text w space replace
    """
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    