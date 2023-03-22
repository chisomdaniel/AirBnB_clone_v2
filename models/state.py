#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
import os
from models.city import City
from models import storage
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

<<<<<<< HEAD
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", order_by=City.id, back_populates="state")
    elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            city_list = []
            for key, value in storage.__objects.items():
                if value.__name__ == 'City':
                    if self.id == value.state_id:
                        city_list.append(value)

            return city_list


City.state = relationship("State", back_populates="cities")
=======
    #if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    cities = relationship("City", order_by=City.id, back_populates="state")
    #elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
    @property
    def cities(self):
        city_list = []
        for key, value in storage.__objects.items():
            if value.__name__ == 'City':
                if self.id == value.state_id:
                    city_list.append(value)

        return city_list

>>>>>>> 5516aaea2b217ddece4da2e25306335256c39f5f
