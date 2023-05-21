#!/usr/bin/python3
'''First flask application'''
from flask import Flask
from flask import render_template
from models import storage
import os


app = Flask(__name__)

states = storage.all('State').values()
amenities = storage.all('Amenity').values()


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    '''Return a template for the states and city under them'''
    new = []
    cities = []
    all_city = {}
    amenity = []
    for i in states:
        cities = []
        new.append(i.name)
        city_list = i.cities
        for j in city_list:
            cities.append(j.name)
        cities = sorted(cities)
        all_city.update({i.name: cities})
    new = sorted(new)
    amenity = [i.name for i in amenities]
    amenity = sorted(amenity)
    return (render_template('10-hbnb_filters.html', states=new,
                            cities=all_city, amenities=amenity))


@app.teardown_appcontext
def close_up(exception):
    '''After each request you must remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
