#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from os import getenv
import sqlalchemy
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_type == 'db':
        __tablename__ = 'cities'
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        name = Column(String(128), nullable=False)

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")

    else:
        __tablename__ = 'cities'
        id = ""
        name = ""
        state_id = ""
