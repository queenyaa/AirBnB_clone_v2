#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import uuid


class Amenity(BaseModel):
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initialize Amenity """
        super().__init__(*args, **kwargs)
