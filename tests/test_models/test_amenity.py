#!/usr/bin/python3
""" """

import pep8
import unittest
from os import getenv
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ """

    @classmethod
    def setUp(self):
        """ setting up """
        self.amenity = Amenity()
        self.amenity.name = "iron"
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_pep8_Amen(self):
        """ pep8 """
        st = pep8.StyleGuide(quiet=True)
        q = st.check_files(['models/amenity.py'])
        self.assertEqual(q.total_errors, 0, 'fix pep8')

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_save(self):
        """ """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
