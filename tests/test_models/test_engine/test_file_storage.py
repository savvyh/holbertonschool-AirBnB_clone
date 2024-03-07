#!/usr/bin/python3
"""This module ti's a file test to the module (file_storage)"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestInitFileStorage(unittest.TestCase):
    """Class to tested each methods from file_storage"""

    def test_init(self):
        """Test initialization of the instance"""
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestMethodFileStorage(unittest.TestCase):
    """Class to tested each methods from file_storage"""

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
        self.base = BaseModel()
        self.store = FileStorage()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        """Cleanup after each test"""
        del self.base
        del self.store
        del self.user
        del self.state
        del self.city
        del self.amenity
        del self.place
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Tests to the method all()"""
        self.assertEqual(dict, type(self.store.all()))
        with self.assertRaises(TypeError):
            self.store.all(None)

    def test_new(self):
        """Tests to the method new()"""
        self.store.new(self.base)
        self.store.new(self.user)
        self.store.new(self.state)
        self.store.new(self.city)
        self.store.new(self.amenity)
        self.store.new(self.place)
        self.store.new(self.review)
        self.assertIn("BaseModel." + self.base.id, self.store.all().keys())
        self.assertIn(self.base, self.store.all().values())
        self.assertIn("User." + self.user.id, self.store.all().keys())
        self.assertIn(self.user, self.store.all().values())
        self.assertIn("State." + self.state.id, self.store.all().keys())
        self.assertIn(self.state, self.store.all().values())
        self.assertIn("City." + self.city.id, self.store.all().keys())
        self.assertIn(self.city, self.store.all().values())
        self.assertIn("Amenity." + self.amenity.id, self.store.all().keys())
        self.assertIn(self.amenity, self.store.all().values())
        self.assertIn("Place." + self.place.id, self.store.all().keys())
        self.assertIn(self.place, self.store.all().values())
        self.assertIn("Review." + self.review.id, self.store.all().keys())
        self.assertIn(self.review, self.store.all().values())
        with self.assertRaises(TypeError):
            self.store.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            self.store.new(None)

    def test_save(self):
        """Tests to the method save()"""
        self.store.new(self.base)
        self.store.new(self.user)
        self.store.new(self.state)
        self.store.new(self.city)
        self.store.new(self.amenity)
        self.store.new(self.place)
        self.store.new(self.review)
        self.store.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)
        with self.assertRaises(TypeError):
            self.store.save(None)

    def test_reload(self):
        """Tests to the method reload()"""
        self.store.new(self.base)
        self.store.new(self.user)
        self.store.new(self.state)
        self.store.new(self.city)
        self.store.new(self.amenity)
        self.store.new(self.place)
        self.store.new(self.review)
        self.store.save()
        self.store.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.base.id, objs)
        self.assertIn("User." + self.user.id, objs)
        self.assertIn("State." + self.state.id, objs)
        self.assertIn("City." + self.city.id, objs)
        self.assertIn("Amenity." + self.amenity.id, objs)
        self.assertIn("Place." + self.place.id, objs)
        self.assertIn("Review." + self.review.id, objs)
        with self.assertRaises(TypeError):
            self.store.reload(None)


if __name__ == "__main__":
    unittest.main()
