#!/usr/bin/python3
"""
unittesting for DBStorage
"""

import unittest
import os
from os import getenv
import pep8
import json
import MySQLdb
from models.base_model import BaseModel, Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """
    DBStorage unittesting
    """
    @classmethod
    def setUp(self):
        """ set up """
        self.User = getenv('HBNB_MYSQL_USER')
        self.Password = getenv('HBNB_MYSQL_PWD')
        self.Db = getenv('HBNB_MYSQL_DB')
        self.host = getenv('HBNB_MYSQL_HOST')
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                                  password=self.Password, db=self.Db,
                                  charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'NO DB')
    def test_DBStor_pep8(self):
        """ pep8 """
        st = pep8.StyleGuide(quiet=True)
        q = st.check_files(['models/engine/db_storage.py'])
        self.assertEqual(q.total_errors, 0, 'fix pep8')

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'NO DB')
    def test_empty_user(self):
        """ no object """
        self.query.execute("SELECT * FROM users")
        sal = self.query.fetchall()
        self.assertEqual(len(sal), 0)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'NO DB')
    def test_table_read(self):
        """ find and read tables """
        self.query.execute("SHOW TABLES")
        sal = self.query.fetchall()
        self.assertEqual(len(sal), 7)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'NO DB')
    def test_adding(self):
        """ adding on """
        self.query.execute("SELECT * FROM states")
        sal = self.query.fetchall()
        self.assertEqual(len(salida), 0)
        state = State(name='LUISILLO')
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        sal = self.query.fetchall()
        self.assertEqual(len(sal), 1)


if __name__ == '__main__':
    unittest.main()
