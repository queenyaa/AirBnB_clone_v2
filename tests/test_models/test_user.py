#!/usr/bin/python3
"""
Testing the User Module of the HBNB Console
"""

import unittest
import os
import pep8
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(unittest.TestCase, test_basemodel):
    """ testing the User Module """
    
    @classmethod
    def setUp(self):
        """ set up the testing """
        self.user = User()
        self.user.first_name = "Queen"
        self.user.last_name = "Bae"
        self.user.email = "queenie@hergrace.com"
        self.user.password = "awEsomesauce"

        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ remove temp storage """
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.remove('tmp', 'file.json')
        except IOError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE' != 'db' else
                         type(None)))

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE' != 'db' else
                         type(None)))

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE' != 'db' else
                         type(None)))

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str if
                         os.getenv('HBNB_TYPE_STORAGE' != 'db' else
                         type(None)))

    def test_User_pep8(self):
        """ testing pep8 of user """
        st = pep8.StyleGuide(quiet=True)
        q = st.check_files(['models/user.py'])
        self.assertEqual(q.total_errors, 0, "fix pep8")

    def test_checking_doc_User(self):
        """ __doc__ of user """
        self.assertIsNotNone(User.__doc__)

    def test_save_User(self):
        """ save """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
