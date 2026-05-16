#!/usr/bin/python3
"""Unit tests for City."""
import unittest
import os
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCityInstantiation(unittest.TestCase):
    """Tests for City instantiation."""

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
        self.assertIsInstance(City(), City)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(City(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(City().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_state_id_is_class_attr(self):
        self.assertIn("state_id", City.__dict__)

    def test_name_is_class_attr(self):
        self.assertIn("name", City.__dict__)

    def test_state_id_default_empty_str(self):
        self.assertEqual(City.state_id, "")

    def test_name_default_empty_str(self):
        self.assertEqual(City.name, "")

    def test_two_unique_ids(self):
        self.assertNotEqual(City().id, City().id)

    def test_in_storage(self):
        c = City()
        self.assertIn("City.{}".format(c.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[City]", str(City()))


class TestCitySave(unittest.TestCase):
    """Tests for City save method."""

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
        c = City()
        old = c.updated_at
        c.save()
        self.assertGreater(c.updated_at, old)

    def test_save_creates_file(self):
        c = City()
        c.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            City().save("unexpected")


class TestCityToDict(unittest.TestCase):
    """Tests for City to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(City().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(City().to_dict()["__class__"], "City")

    def test_has_id(self):
        self.assertIn("id", City().to_dict())

    def test_dates_are_strings(self):
        d = City().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            City().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
