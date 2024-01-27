#!/usr/bin/python3
"""This module defines a class User"""

import hashlib
from sqlalchemy import Column, String
from models.base_model import BaseModel
import models
import uuid
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    id = Column(String(60), nullable=False, primary_key=True,
                default=lambda: str(uuid.uuid4()))
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", backref="users",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="users",
                               cascade="all, delete, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """ initializing the class user """
        super().__init__(*args, **kwargs)
