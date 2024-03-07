#!/usr/bin/python3
"""This module it's a test_module to (base_model)"""
import unittest
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """This is the Test Class for the module (base_model)"""

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
        self.bm = BaseModel()

    def tearDown(self):
        """Cleanup after each test"""
        del self.bm
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_init_create(self):
        """Test the initalization of instance created"""
        self.assertIsInstance(self.bm, BaseModel)
        self.assertIsNotNone(self.bm.id)
        self.assertIsNotNone(self.bm.created_at)
        self.assertIsNotNone(self.bm.updated_at)

    def test_init_recreate(self):
        """Test the process to recreate an instance with kwargs"""
        bm_dict = self.bm.to_dict()
        new_obj_bm = BaseModel(**bm_dict)
        self.assertEqual(self.bm.id, new_obj_bm.id)
        self.assertEqual(self.bm.created_at, new_obj_bm.created_at)
        self.assertEqual(self.bm.updated_at, new_obj_bm.updated_at)
        self.assertEqual(self.bm.__dict__, new_obj_bm.__dict__)
        self.assertEqual(self.bm.to_dict(), new_obj_bm.to_dict())
        self.assertIsInstance(new_obj_bm.created_at, datetime.datetime)
        self.assertIsInstance(new_obj_bm.updated_at, datetime.datetime)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.bm.__class__.__name__, str(self.bm))
        self.assertIn(self.bm.id, str(self.bm))
        self.assertIn(str(self.bm.__dict__), str(self.bm))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(self.bm.updated_at, initial_updated)
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + self.bm.id, save_text)
        with self.assertRaises(TypeError):
            self.bm.save(None)

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        dict_bm = self.bm.to_dict()
        self.assertIsInstance(dict_bm, dict)
        self.assertNotEqual(dict_bm, self.bm.__dict__)
        self.assertEqual(dict_bm["__class__"], 'BaseModel')
        self.assertEqual(dict_bm['id'], self.bm.id)
        self.assertEqual(dict_bm['created_at'], self.bm.created_at.isoformat())
        self.assertEqual(dict_bm["updated_at"], self.bm.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
