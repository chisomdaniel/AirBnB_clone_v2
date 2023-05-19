#!/usr/bin/python3
'''First flask application'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Return a simple Hello world text'''
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Return a simpler text'''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''C is fun'''
    text = text.replace('_', ' ')
    return (f"C {text}")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    '''Python is cool'''
    text = text.replace('_', ' ')
    return (f"Python {text}")


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    '''check if it is a number'''
    return (f"{n} is a number")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
