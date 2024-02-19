#!/usr/bin/python3
""" Place Module for HBNB project """

import models
import uuid
from models.base_model import BaseModel
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table

Base = declarative_base()

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        city_id = Column(String(60), ForeignKey("cities.id"),
                         nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade='all, delete',
                               backref='places')
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False, backref='place_amenities')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ initializing place class"""
        super().__init__(*args, **kwargs)

    @property
    def  reviews(self):
        """ return the Review list """
        val_rev = models.storage.all("Review").values()
        rev_list = []
        for review in val_rev:
            if review.place_ist == self.id:
                rev_list.append(review)
        return rev_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """ return Amenity list """
            val_amen = models.storage.all("Amenity").values()
            amen_list = []
            for amenity in val_amen:
                if amenity.place_id == self.id:
                    amen_list.append(amenity)
            return amen_list

        @amenities.setter
        def amenities(self, obj=None):
            """ Set amenity id """
            if type(obj).__name__ == 'Amenity':
                n_amenity = 'Amenity' + '.' + obj.id
                self.amenity_ids.append(n_amenity)
