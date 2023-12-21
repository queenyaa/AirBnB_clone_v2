#!/usr/bin/python3
"""
unittesting for the Review Module
"""

import unittest
import os
from models.base_model import BaseModel
from models.review import Review
import pep8
import json


class TestReview(unittest.TestCase):
    """ the testing """

    @classmethod
    def setUp(self):
        """ settin up """
        self.revie = Review()
        self.revie.place_id = "3243-ghfj"
        self.revie.user_id = "queenieB"
        self.revie.text = "O I enjoyed myself over there"
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ delete testign """
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
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_pep8_reviews(self):
        """ pep8 testing """
        st = pep8.StyleGuide(quiet = True)
        q = st.check_files(['models/review.py'])
        self.assertEqual(q.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] == 'db',
                     'Invalid storage mode')
    def test_save_reviews(self):
        """ saving testing """
        self.revie.save()
        self.assertNotEqual(self.revie.created_at, self.revie.updated_at)


if __name__ == '__main__':
    unittest.main()
