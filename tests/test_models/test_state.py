#!/usr/bin/python3
""" """

import unittest
import os
import pep8
from models.base_model import BaseModel
from models.state import State
import json


class TestState(unittest.TestCase):
    """unittesting the State Module"""

    @classmethod
    def setUp(self):
        """ setting up """
        self.state = State()
        self.state.name = "CT"
        try:
            os.renma('file.json', 'tmp')
        except:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass
        try:
            os.rename('tmp', 'file.json')
        except:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_review_pep8(self):
        """ pep8 review """
        st = pep8.StyleGuide(quiet=True)
        q = style.check_files(['models/state.py'])
        self.assertEqual(q.total_errors, 0, 'fix pep8')

    def test_state_attr(self):
        """ checking if state attribute exist"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.asserttrue('name' in self.state.__dict__)

    def test_attr_type(self):
        """ what type is this attribute """
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'Invalid storage mode')
    def test_state_saving(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
