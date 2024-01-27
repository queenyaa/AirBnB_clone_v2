#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from os import getenv
import models

t_fmt = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = kwargs['created_at']

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        if type(self.created_at) is str:
            self.created_at = datetime.strptime(self.created_at, t_fmt)
        if type(self.updated_at) is str:
            self.updated_at = datetime.strptime(self.updated_at, t_fmt)

    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # cls = type(self).__name__
        return ('[{:s}] ({:s}) {}'.format(self.__class__.__name__,
                                          self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """Convert instance into dict format"""
        n_dict = self.__dict__.copy()
        # dictionary.update(self.__dict__)
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].isoformat()
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()
        if "_password" in n_dict:
            n_dict["password"] = n_dict["_password"]
            n_dict.pop('_password', None)
        if 'amenities' in n_dict:
            n_dict.pop('amenities', None)
        if 'reviews' in n_dict:
            n_dict.pop('reviews', None)
        n_dict['__class__'] = self.__class__.__name__
        n_dict.pop('_sa_instance_state', None)
        if not save_to_disk:
            n_dict.pop('password', None)
        return n_dict

    def delete(self):
        models.storage.delete(self)
