#!/usr/bin/python3
"""Module it's a test file to the module (user)"""
import os
import models
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

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
        self.user = User()

    def tearDown(self):
        """Cleanup after each test"""
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_User(self):
        """Test init class User"""
        self.assertEqual(type(self.user), User)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(str, type(self.user.email))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(str, type(self.user.password))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(str, type(self.user.first_name))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(str, type(self.user.last_name))
        self.assertIn("{}.{}".format(self.user.__class__.__name__,
                                     self.user.id),
                      models.storage._FileStorage__objects)

    def test_inherit_user(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsNotNone(self.user.id)
        self.assertEqual(str, type(self.user.id))
        self.assertIsNotNone(self.user.created_at)
        self.assertEqual(datetime, type(self.user.created_at))
        self.assertIsNotNone(self.user.updated_at)
        self.assertEqual(datetime, type(self.user.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        user_dict = self.user.to_dict()
        user_cpy = User(**user_dict)
        self.assertEqual(self.user.id, user_cpy.id)
        self.assertEqual(self.user.created_at, user_cpy.created_at)
        self.assertEqual(self.user.updated_at, user_cpy.updated_at)
        self.assertEqual(self.user.__dict__, user_cpy.__dict__)
        self.assertEqual(self.user.to_dict(), user_cpy.to_dict())
        self.assertIsInstance(user_cpy.created_at, datetime)
        self.assertIsInstance(user_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.user.__class__.__name__,
                                     self.user.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.user.__class__.__name__, str(self.user))
        self.assertIn(self.user.id, str(self.user))
        self.assertIn(str(self.user.__dict__), str(self.user))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertNotEqual(user_dict, self.user.__dict__)
        self.assertEqual(user_dict["__class__"], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"],
                         self.user.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
