#!/usr/bin/python3
"""
Unit tests for the City class.
"""

import unittest
import pycodestyle
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the test.
        """
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """
        Tear down after the test.
        """
        del cls.city

    def tearDown(self):
        """
        Tear down for each test method.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_compliance(self):
        """
        Test PEP8 compliance for City class.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_docstrings(self):
        """
        Test if docstrings are present.
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """
        Test if City has the expected attributes.
        """
        attributes = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.city, attribute))

    def test_is_subclass(self):
        """
        Test if City is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types(self):
        """
        Test attribute types for City.
        """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_method(self):
        """
        Test if the save method works.
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method works.
        """
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()
