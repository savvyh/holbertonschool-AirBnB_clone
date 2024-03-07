#!/usr/bin/python3
"""Module it's a test file to the module (review)"""
import os
import models
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

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
        self.review = Review()

    def tearDown(self):
        """Cleanup after each test"""
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_Review(self):
        """Test init class Review"""
        self.assertEqual(type(self.review), Review)
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(str, type(self.review.place_id))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(str, type(self.review.user_id))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(str, type(self.review.text))
        self.assertIn("{}.{}".format(self.review.__class__.__name__,
                                     self.review.id),
                      models.storage._FileStorage__objects)

    def test_inherit_Review(self):
        """Test init from inheritance attribut (BaseModel)"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsNotNone(self.review.id)
        self.assertEqual(str, type(self.review.id))
        self.assertIsNotNone(self.review.created_at)
        self.assertEqual(datetime, type(self.review.created_at))
        self.assertIsNotNone(self.review.updated_at)
        self.assertEqual(datetime, type(self.review.updated_at))

    def test_init_kwargs(self):
        """Test the process to recreate an instance with kwargs"""
        review_dict = self.review.to_dict()
        review_cpy = Review(**review_dict)
        self.assertEqual(self.review.id, review_cpy.id)
        self.assertEqual(self.review.created_at, review_cpy.created_at)
        self.assertEqual(self.review.updated_at, review_cpy.updated_at)
        self.assertEqual(self.review.__dict__, review_cpy.__dict__)
        self.assertEqual(self.review.to_dict(), review_cpy.to_dict())
        self.assertIsInstance(review_cpy.created_at, datetime)
        self.assertIsInstance(review_cpy.updated_at, datetime)
        self.assertIn("{}.{}".format(self.review.__class__.__name__,
                                     self.review.id),
                      models.storage._FileStorage__objects)

    def test_str_method(self):
        """Test if all attributes are inside the str representation"""
        self.assertIn(self.review.__class__.__name__, str(self.review))
        self.assertIn(self.review.id, str(self.review))
        self.assertIn(str(self.review.__dict__), str(self.review))

    def test_save_method(self):
        """Test if the save method well update attribute (updated_at)"""
        initial_updated = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, initial_updated)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test if well created a dict and this contains all informations
        on the object"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertNotEqual(review_dict, self.review.__dict__)
        self.assertEqual(review_dict["__class__"], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         self.review.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
