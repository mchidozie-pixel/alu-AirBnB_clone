#!/usr/bin/python3
"""Unit tests for Amenity."""
import unittest
import os
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestAmenityInstantiation(unittest.TestCase):
    """Tests for Amenity instantiation."""

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
        self.assertIsInstance(Amenity(), Amenity)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(Amenity(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(Amenity().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(Amenity().updated_at, datetime)

    def test_name_is_class_attr(self):
        self.assertIn("name", Amenity.__dict__)

    def test_name_default_empty_str(self):
        self.assertEqual(Amenity.name, "")

    def test_two_unique_ids(self):
        self.assertNotEqual(Amenity().id, Amenity().id)

    def test_in_storage(self):
        a = Amenity()
        self.assertIn("Amenity.{}".format(a.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[Amenity]", str(Amenity()))


class TestAmenitySave(unittest.TestCase):
    """Tests for Amenity save method."""

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
        a = Amenity()
        old = a.updated_at
        a.save()
        self.assertGreater(a.updated_at, old)

    def test_save_creates_file(self):
        a = Amenity()
        a.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Amenity().save("unexpected")


class TestAmenityToDict(unittest.TestCase):
    """Tests for Amenity to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(Amenity().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(Amenity().to_dict()["__class__"], "Amenity")

    def test_has_id(self):
        self.assertIn("id", Amenity().to_dict())

    def test_dates_are_strings(self):
        d = Amenity().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Amenity().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
