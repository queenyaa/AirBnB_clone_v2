#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
import os


# define the storage variable
storage = None

storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # import and create an instance of FileStorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage data
storage.reload()
