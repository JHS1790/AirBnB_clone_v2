#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade='all, delete',
                              backref='state')

    else:
        @property
        def cities(self):
            """getter for cities"""
            #if getenv('HBNB_TYPE_STORAGE') != 'db':
            from models import storage
            cities_list = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
