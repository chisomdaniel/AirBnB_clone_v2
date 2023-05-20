#!/usr/bin/python3
'''First flask application'''
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)
states = storage.all('State').values()


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Return a template for the states'''
    new = {}
    for i in states:
        new[i.name] = i.id
    names = list(new.keys())
    return (render_template('7-states_list.html', state_dict=new, names=names))


@app.teardown_appcontext
def close_up(exception):
    '''After each request you must remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
