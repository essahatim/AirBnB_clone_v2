#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv
import pycodestyle
import unittest

storage_type = getenv("HBNB_TYPE_STORAGE")


class TestAmenityModel(test_basemodel):
    """
    Test cases for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """Initialize test case."""
        super().__init__(*args, **kwargs)
        self.model_name = "Amenity"
        self.model = Amenity

    def test_name_type(self):
        """Test type of the 'name' attribute."""
        new_instance = self.model()
        self.assertEqual(type(new_instance.name), str)


class TestPEP8(unittest.TestCase):
    """
    Test case for checking PEP8 compliance.
    """

    def test_pep8_compliance(self):
        """Check PEP8 compliance for Amenity class."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestInheritBaseModel(unittest.TestCase):
    """
    Test case for checking inheritance from BaseModel.
    """

    def test_instance(self):
        """Check if Amenity inherits from BaseModel."""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))
        self.assertEqual(
            str(type(amenity_instance)),
            "<class 'models.amenity.Amenity'>"
            )


class TestAmenityBaseModel(unittest.TestCase):
    """
    Test cases for the Amenity class inheriting from BaseModel.
    """

    def test_instance_attributes(self):
        """Check instance attributes."""
        with patch('models.amenity'):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expected_attr_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    }
            instance_dict = instance.to_dict()
            expected_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"
                    ]
            self.assertCountEqual(instance_dict.keys(), expected_attrs)
            self.assertEqual(instance_dict['name'], 'Barbie')
            self.assertEqual(instance_dict['__class__'], 'Amenity')

            for attr, types in expected_attr_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_id_and_created_at(self):
        """Check ID and creation time."""
        amenity_1 = Amenity()
        sleep(2)
        amenity_2 = Amenity()
        sleep(2)
        amenity_3 = Amenity()
        sleep(2)
        list_amenities = [amenity_1, amenity_2, amenity_3]
        for instance in list_amenities:
            instance_id = instance.id
            with self.subTest(instance_id=instance_id):
                self.assertIs(type(instance_id), str)
        self.assertNotEqual(amenity_1.id, amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_3.id)
        self.assertNotEqual(amenity_2.id, amenity_3.id)
        self.assertTrue(amenity_1.created_at <= amenity_2.created_at)
        self.assertTrue(amenity_2.created_at <= amenity_3.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_2.created_at)
        self.assertNotEqual(amenity_1.created_at, amenity_3.created_at)
        self.assertNotEqual(amenity_3.created_at, amenity_2.created_at)

    def test_str_method(self):
        """Test __str__ method."""
        instance = Amenity()
        expected_output = "[Amenity] ({}) {}".format(
                instance.id,
                instance.__dict__
                )
        self.assertEqual(expected_output, str(instance))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Test save method."""
        instance = Amenity()
        created_at = instance.created_at
        sleep(2)
        updated_at = instance.updated_at
        instance.save()
        new_created_at = instance.created_at
        sleep(2)
        new_updated_at = instance.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel."""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, BaseModel)
        self.assertTrue(hasattr(amenity_instance, "id"))
        self.assertTrue(hasattr(amenity_instance, "created_at"))
        self.assertTrue(hasattr(amenity_instance, "updated_at"))

    def test_name_attribute(self):
        """Test existence and type of the 'name' attribute."""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, "name"))
        if storage_type == 'db':
            self.assertEqual(amenity_instance.name, None)
        else:
            self.assertEqual(amenity_instance.name, "")

    def test_to_dict_method(self):
        """Test to_dict method."""
        amenity_instance = Amenity()
        new_dict = amenity_instance.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in amenity_instance.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test values returned by to_dict method."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity_instance = Amenity()
        new_dict = amenity_instance.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         amenity_instance.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         amenity_instance.updated_at.strftime(t_format))

    def test_str_method(self):
        """Test str method."""
        amenity_instance = Amenity()
        string = "[Amenity] ({}) {}".format(
                amenity_instance.id,
                amenity_instance.__dict__
                )
        self.assertEqual(string, str(amenity_instance))
