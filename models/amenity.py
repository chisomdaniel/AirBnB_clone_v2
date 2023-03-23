#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Amenity class'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    #place_amenities = relationship("Place", back_populates="amenities")

