#!/usr/bin/python3
'''First flask application'''
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)
states = storage.all('State')


@app.route('/states', strict_slashes=False)
def states_list():
    '''Return a template for the states'''
    new = {}
    for i in states.values():
        new[i.name] = i.id

    return (render_template('9-states.html', id=False, state_dict=new))


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    '''Display the state by id given'''
    cities = {}
    for i in states.values():
        if id == i.id:
            print("If passed")
            state = i
            city_list = i.cities
            for j in city_list:
                cities[j.name] = j.id

            return (render_template('9-states.html', id=id, error='False',
                                    state=state, cities=cities))

    return (render_template('9-states.html', error='404', id=id))


@app.teardown_appcontext
def close_up(exception):
    '''After each request you must remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
