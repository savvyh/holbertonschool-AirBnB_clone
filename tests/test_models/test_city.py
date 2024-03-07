#!/usr/bin/python3
"""Module it's a test file to the module (city)"""
import os
import models
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

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
        self.city = City()

    def tearDown(self):
        """Cleanup after each test"""
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_City(self):
        """Test init class City"""
        self.assertEqual(type(self.city), City)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(str, type(self.city.name))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(str, type(self.city.state_id))
        self.assertIn("{}.{}".format(self.city.__class__.__name__,
                                     self.city.id),
                      models.storage._FileStorage__objects)

    def test_inherit_City(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsNotNone(self.city.id)
        self.assertEqual(str, type(self.city.id))
        self.assertIsNotNone(self.city.created_at)
        self.assertEqual(datetime, type(self.city.created_at))
        self.assertIsNotNone(self.city.updated_at)
        self.assertEqual(datetime, type(self.city.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        city_dict = self.city.to_dict()
        city_cpy = City(**city_dict)
        self.assertEqual(self.city.id, city_cpy.id)
        self.assertEqual(self.city.created_at, city_cpy.created_at)
        self.assertEqual(self.city.updated_at, city_cpy.updated_at)
        self.assertEqual(self.city.__dict__, city_cpy.__dict__)
        self.assertEqual(self.city.to_dict(), city_cpy.to_dict())
        self.assertIsInstance(city_cpy.created_at, datetime)
        self.assertIsInstance(city_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.city.__class__.__name__,
                                     self.city.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.city.__class__.__name__, str(self.city))
        self.assertIn(self.city.id, str(self.city))
        self.assertIn(str(self.city.__dict__), str(self.city))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertNotEqual(city_dict, self.city.__dict__)
        self.assertEqual(city_dict["__class__"], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"],
                         self.city.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
