#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""
import inspect
import os
import pycodestyle
import unittest
from datetime import datetime
from models.engine import db_storage
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

DBStorage = db_storage.DBStorage
storage_type = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.db_storage_functions = inspect.getmembers(
                DBStorage,
                inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/'
                                    'test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_db_storage_functions_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.db_storage_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    @unittest.skipIf(storage_type != 'db', "Not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_type != 'db', "Not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        all_states = models.storage.all()
        self.assertEqual(models.storage.all(), all_states)

    @unittest.skipIf(storage_type != 'db', "Not testing db storage")
    def test_new(self):
        """Test that new adds an object to the database"""
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        all_states = models.storage.all()
        self.assertIn(new_state, all_states.values())

    @unittest.skipIf(storage_type != 'db', "Not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        with open('file.json', 'r') as f:
            content = f.read()
            self.assertIn(new_state.to_dict(), content)


if __name__ == "__main__":
    unittest.main()
