#!/usr/bin/python3

"""
Unittesting the console of HBNB
"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Unittest this console
    """

    @classmethod
    def setUp(cls):
        """ setting up the unittest """
        cls.consol = HBNBCommand()

    @classmethod
    def tearDown(cls):
        """ close the unittest """
        del cls.consol

    def tearDown(self):
        """ delete testing from temporary file """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_console_pep8(self):
        """ test pep8 """
        st = pep8.StyleGuide(quiet=True)
        v = st.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_line_empty(self):
        """ this line must be empty """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_e_quit(self):
        """ quitting the console """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_console_docstrings(self):
        """ check for docstrings in console """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_do_create(self):
        """ Testing the create command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                    "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self. assertEqual(
                    "** class deesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="em@hbnb.com" password=234')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")

    def test_EOF(self):
        """ End Of Line existence """
        consol = self.HBNBCommnad()
        self.assertTrue(console.onecmd("quit"))

    def test_all(self):
        """ all exists """
        consol = self.HBNBCommand()
        consol.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str()))

    def test_show(show):
        """
        Test the show message
        """
        consol = self.HBNBCommand()
        consol.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        consol.onecmd("show User")
        y = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", y)

    @unittest.skipIf(db == 'db', 'Testing databse storage only')
    def test_no_instan_found(self):
        """
        Test show message error id missing
        """
        consol = self.HBNBCommand()
        consol.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        consol.onecmd("show User " + "234321238")
        y = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", y)


    @unittest.skipIf(db != 'db', "Testing DBStorage only")
    def test_db_create(self):
        """ test creating DBStorage """
        consol = self.HBNBCommand()
        consol.onecmd("create State name=California")
        res = storage.all("State")
        self.assertTrue(len(res) > 0)

    def test_destroy(self):
        """ the destroy function unittesting """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy Jake")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 234321")
            self.assertEqual("** no instance found **\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
