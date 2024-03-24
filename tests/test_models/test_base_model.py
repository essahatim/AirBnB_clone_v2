#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
import datetime
import json
import os
import pycodestyle
import inspect
from models.base_model import BaseModel
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """Set up for each test."""
        pass

    def tearDown(self):
        """Tear down after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_compliance(self):
        """
        Test PEP8 compliance for BaseModel class.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """
        Test if docstrings are present for all methods.
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_existence(self):
        """
        Test if all expected methods exist in BaseModel.
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_base_model(self):
        """
        Test if BaseModel instance is created properly.
        """
        base_model_instance = BaseModel()
        self.assertTrue(isinstance(base_model_instance, BaseModel))

    def test_save_method(self):
        """
        Test if the save method updates the timestamps.
        """
        base_model_instance = BaseModel()
        created_at = base_model_instance.created_at
        base_model_instance.save()
        updated_at = base_model_instance.updated_at
        self.assertNotEqual(created_at, updated_at)

    def test_to_dict_method(self):
        """
        Test if BaseModel instance can be converted to dictionary.
        """
        base_model_instance = BaseModel()
        base_dict = base_model_instance.to_dict()
        self.assertEqual(base_model_instance.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_uuid_generation(self):
        """
        Test if UUIDs are generated properly for BaseModel instances.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        instance_list = [instance1, instance2, instance3]
        for instance in instance_list:
            self.assertIs(type(instance.id), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """
        Test if the string representation of BaseModel is correct.
        """
        instance = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(
                                                        instance.id,
                                                        instance.__dict__)
        self.assertEqual(expected_output, str(instance))


if __name__ == "__main__":
    unittest.main()
