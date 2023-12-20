#!/usr/bin/python3
""" """

import unittest
import os
import pep8
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(unittest.TestCase, test_basemodel):
    """ """
    @classmethod
    def setUp(self):
        self.place = Place()
        self.place.user_id = "5432-cdcd"
        self.place.city_id = "6543-hjhj"
        self.place.name = "Bo Yah"
        self.place.description = "Interesting"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.placee.price_by_night = 21
        self.place.latitude = 121.0
        self.place.longitude = 5.0
        self.place.amenity_ids = ["3243-jkjkjkj"]

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
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'DB')
    def test_save_place(self):
        """ if saving to database works """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)
    
    def test_to_dict_Place(self):
        """ if dictionary works """
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ = "__main__":
    unittest.main()
