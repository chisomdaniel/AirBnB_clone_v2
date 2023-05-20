#!/usr/bin/python3
'''First flask application'''
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)
states = storage.all('State').values()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    '''Return a template for the states and city under them'''
    new = {}
    cities = {}
    all_city = {}
    for i in states:
        cities = {}
        new[i.name] = i.id
        city_list = i.cities
        for j in city_list:
            cities[j.name] = j.id
        all_city.update({i.name: cities})

    names = list(new.keys())
    return (render_template('8-cities_by_states.html', state_dict=new, names=names, cities=all_city))


@app.teardown_appcontext
def close_up(exception):
    '''After each request you must remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
