#!/usr/bin/python3
"""Module it's a test file to the module (place)"""
import os
import models
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

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
        self.place = Place()

    def tearDown(self):
        """Cleanup after each test"""
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_Place(self):
        """Test init class Place"""
        self.assertEqual(type(self.place), Place)
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(str, type(self.place.city_id))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(str, type(self.place.user_id))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(str, type(self.place.name))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(str, type(self.place.description))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(int, type(self.place.number_rooms))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(int, type(self.place.number_bathrooms))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(int, type(self.place.max_guest))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(int, type(self.place.price_by_night))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(float, type(self.place.latitude))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(float, type(self.place.longitude))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(list, type(self.place.amenity_ids))
        self.assertIn("{}.{}".format(self.place.__class__.__name__,
                                     self.place.id),
                      models.storage._FileStorage__objects)

    def test_inherit_Place(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsNotNone(self.place.id)
        self.assertEqual(str, type(self.place.id))
        self.assertIsNotNone(self.place.created_at)
        self.assertEqual(datetime, type(self.place.created_at))
        self.assertIsNotNone(self.place.updated_at)
        self.assertEqual(datetime, type(self.place.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        place_dict = self.place.to_dict()
        place_cpy = Place(**place_dict)
        self.assertEqual(self.place.id, place_cpy.id)
        self.assertEqual(self.place.created_at, place_cpy.created_at)
        self.assertEqual(self.place.updated_at, place_cpy.updated_at)
        self.assertEqual(self.place.__dict__, place_cpy.__dict__)
        self.assertEqual(self.place.to_dict(), place_cpy.to_dict())
        self.assertIsInstance(place_cpy.created_at, datetime)
        self.assertIsInstance(place_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.place.__class__.__name__,
                                     self.place.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.place.__class__.__name__, str(self.place))
        self.assertIn(self.place.id, str(self.place))
        self.assertIn(str(self.place.__dict__), str(self.place))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertNotEqual(place_dict, self.place.__dict__)
        self.assertEqual(place_dict["__class__"], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         self.place.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
