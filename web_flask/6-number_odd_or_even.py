#!/usr/bin/python3
'''First flask application'''
from flask import Flask
from flask import render_template


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
    return ("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    '''Python is cool'''
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    '''check if it is a number'''
    return ("{n} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def int_template(n):
    '''check if it is a number and pass to a template'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    '''check if the number is even or odd'''
    if int(n) % 2 == 0:
        text = "{} is even".format(n)
        return render_template('6-number_odd_or_even.html', n=text)
    else:
        text = "{} is odd".format(n)
        return render_template('6-number_odd_or_even.html', n=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
