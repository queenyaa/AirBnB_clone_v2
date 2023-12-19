#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    # for DBStorage
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                cascade="all, delete, delete-orphan")

    # For FileStorage
    else:
        name = ""

        @property
        def cities(self):
            """ Getter attribute that returns the list of City instances """
            city_list = []
            for city in models.storage.all(models.City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)
