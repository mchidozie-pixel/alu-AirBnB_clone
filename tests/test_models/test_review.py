#!/usr/bin/python3
"""Unit tests for Review."""
import unittest
import os
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReviewInstantiation(unittest.TestCase):
    """Tests for Review instantiation."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_instantiates(self):
        self.assertIsInstance(Review(), Review)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(Review(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(Review().id, str)

    def test_place_id_is_class_attr(self):
        self.assertIn("place_id", Review.__dict__)

    def test_user_id_is_class_attr(self):
        self.assertIn("user_id", Review.__dict__)

    def test_text_is_class_attr(self):
        self.assertIn("text", Review.__dict__)

    def test_place_id_default_empty_str(self):
        self.assertEqual(Review.place_id, "")

    def test_user_id_default_empty_str(self):
        self.assertEqual(Review.user_id, "")

    def test_text_default_empty_str(self):
        self.assertEqual(Review.text, "")

    def test_two_unique_ids(self):
        self.assertNotEqual(Review().id, Review().id)

    def test_in_storage(self):
        r = Review()
        self.assertIn("Review.{}".format(r.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[Review]", str(Review()))


class TestReviewSave(unittest.TestCase):
    """Tests for Review save method."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_save_updates_updated_at(self):
        r = Review()
        old = r.updated_at
        r.save()
        self.assertGreater(r.updated_at, old)

    def test_save_creates_file(self):
        r = Review()
        r.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Review().save("unexpected")


class TestReviewToDict(unittest.TestCase):
    """Tests for Review to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(Review().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(Review().to_dict()["__class__"], "Review")

    def test_has_id(self):
        self.assertIn("id", Review().to_dict())

    def test_dates_are_strings(self):
        d = Review().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Review().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
