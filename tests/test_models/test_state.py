#!/usr/bin/python3
"""Module it's a test file to the module (state)"""
import os
import models
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

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
        self.state = State()

    def tearDown(self):
        """Cleanup after each test"""
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_State(self):
        """Test init class state"""
        self.assertEqual(type(self.state), State)
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(str, type(self.state.name))
        self.assertIn("{}.{}".format(self.state.__class__.__name__,
                                     self.state.id),
                      models.storage._FileStorage__objects)

    def test_inherit_State(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsNotNone(self.state.id)
        self.assertEqual(str, type(self.state.id))
        self.assertIsNotNone(self.state.created_at)
        self.assertEqual(datetime, type(self.state.created_at))
        self.assertIsNotNone(self.state.updated_at)
        self.assertEqual(datetime, type(self.state.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        state_dict = self.state.to_dict()
        state_cpy = State(**state_dict)
        self.assertEqual(self.state.id, state_cpy.id)
        self.assertEqual(self.state.created_at, state_cpy.created_at)
        self.assertEqual(self.state.updated_at, state_cpy.updated_at)
        self.assertEqual(self.state.__dict__, state_cpy.__dict__)
        self.assertEqual(self.state.to_dict(), state_cpy.to_dict())
        self.assertIsInstance(state_cpy.created_at, datetime)
        self.assertIsInstance(state_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.state.__class__.__name__,
                                     self.state.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.state.__class__.__name__, str(self.state))
        self.assertIn(self.state.id, str(self.state))
        self.assertIn(str(self.state.__dict__), str(self.state))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertNotEqual(state_dict, self.state.__dict__)
        self.assertEqual(state_dict["__class__"], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         self.state.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
