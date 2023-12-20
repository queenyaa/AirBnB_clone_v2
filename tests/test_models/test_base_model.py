#!/usr/bin/python3
""" """

from models.base_model import BaseModel
import unittest
import datetime
from os import getenv
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """ to test the BaseModel Module  """

    @classmethod
    def setUp(self):
        self.base = BaseModel()
        self.base.names = "Afi"
        self.base.num =40

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
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertFalse(new.created_at == new.updated_at)
        else:
            self.assertIsNone(new.created_at)

    def test_pep8_BaseModel(self):
        """ testing pep8 of BaseModel Module """
        st = pep8.StyleGuide(quiet=True)
        q = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") = 'db', 'DB')
    def test_BaseModel_saving(self):
        """ test the saving BaseModel """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)


if __name__ = "__main__":
    unittest.main()
