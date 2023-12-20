#!/usr/bin/python3
""" """

import unittest
import os
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class TestCity(unittest.TestCase, test_basemodel):
    """ """

    @classmethod
    def setUp(self):
        """ set up """
        self.city = City()
        self.city.name = "Hartford"
        self.city.state_id = "CT"
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

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_city_pep8(self):
        """ pep8 testing """
        st = pep8.StyleGuide(quiet=True)
        q = st.check_files(['models/city.py'])
        self.assertEqual(q.total_errors, 0, 'fix pep8')

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'DB')
    def test_saving(self):
        """ savings """
        self.city.save()
        self.assertNotEqual(self.city.create_at, self.city.updated_at)


if __name__ == '__main__':
    unittest.main()
