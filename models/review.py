#!/usr/bin/python3
""" Review module for the HBNB project """

import models
from models.base_model import BaseModel
from os import getenv
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    if models.storage_type == 'db':
        __tablename__ = 'reviews'
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),
                         nullable=False)

    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """ initializing the class Review """
        super().__init__(*args, **kwargs)
