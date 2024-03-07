#!/usr/bin/python3
"""Module it's a test file to the module (amenity)"""
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Setup to change name to JSON file"""
        try:
            os.rename("file.json", "buffer_save.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Rename JSON file with well name"""
        try:
            os.rename("buffer_save.json", "file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """Setup for each test"""
        self.amenity = Amenity()

    def tearDown(self):
        """Cleanup after each test"""
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_Amenity(self):
        """Test init class Amenity"""
        self.assertEqual(type(self.amenity), Amenity)
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(str, type(self.amenity.name))
        self.assertIn("{}.{}".format(self.amenity.__class__.__name__,
                                     self.amenity.id),
                      models.storage._FileStorage__objects)

    def test_inherit_Amenity(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsNotNone(self.amenity.id)
        self.assertEqual(str, type(self.amenity.id))
        self.assertIsNotNone(self.amenity.created_at)
        self.assertEqual(datetime, type(self.amenity.created_at))
        self.assertIsNotNone(self.amenity.updated_at)
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        amenity_dict = self.amenity.to_dict()
        amenity_cpy = Amenity(**amenity_dict)
        self.assertEqual(self.amenity.id, amenity_cpy.id)
        self.assertEqual(self.amenity.created_at, amenity_cpy.created_at)
        self.assertEqual(self.amenity.updated_at, amenity_cpy.updated_at)
        self.assertEqual(self.amenity.__dict__, amenity_cpy.__dict__)
        self.assertEqual(self.amenity.to_dict(), amenity_cpy.to_dict())
        self.assertIsInstance(amenity_cpy.created_at, datetime)
        self.assertIsInstance(amenity_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.amenity.__class__.__name__,
                                     self.amenity.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.amenity.__class__.__name__, str(self.amenity))
        self.assertIn(self.amenity.id, str(self.amenity))
        self.assertIn(str(self.amenity.__dict__), str(self.amenity))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertNotEqual(amenity_dict, self.amenity.__dict__)
        self.assertEqual(amenity_dict["__class__"], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         self.amenity.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
