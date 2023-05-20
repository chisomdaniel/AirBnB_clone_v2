#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
import os
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    cities = relationship("City", order_by=City.id, back_populates="state")
    # elif os.getenv('HBNB_TYPE_STORAGE') == 'file':

    @property
    def cities(self):
        '''to define the relationship for cities'''
        from models import storage

        city_list = []
        for key, value in storage.all(City).items():
            # if value.__name__ == 'City':
            if self.id == value.state_id:
                city_list.append(value)

        return city_list
