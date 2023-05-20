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
    out = "C {}".format(text)
    return (out)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
