#!/usr/bin/python3
"""Unit tests for Place."""
import unittest
import os
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlaceInstantiation(unittest.TestCase):
    """Tests for Place instantiation."""

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
        self.assertIsInstance(Place(), Place)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(Place().id, str)

    def test_city_id_is_class_attr(self):
        self.assertIn("city_id", Place.__dict__)

    def test_user_id_is_class_attr(self):
        self.assertIn("user_id", Place.__dict__)

    def test_name_is_class_attr(self):
        self.assertIn("name", Place.__dict__)

    def test_description_is_class_attr(self):
        self.assertIn("description", Place.__dict__)

    def test_number_rooms_is_class_attr(self):
        self.assertIn("number_rooms", Place.__dict__)

    def test_number_bathrooms_is_class_attr(self):
        self.assertIn("number_bathrooms", Place.__dict__)

    def test_max_guest_is_class_attr(self):
        self.assertIn("max_guest", Place.__dict__)

    def test_price_by_night_is_class_attr(self):
        self.assertIn("price_by_night", Place.__dict__)

    def test_latitude_is_class_attr(self):
        self.assertIn("latitude", Place.__dict__)

    def test_longitude_is_class_attr(self):
        self.assertIn("longitude", Place.__dict__)

    def test_amenity_ids_is_class_attr(self):
        self.assertIn("amenity_ids", Place.__dict__)

    def test_city_id_default_empty_str(self):
        self.assertEqual(Place.city_id, "")

    def test_number_rooms_default_zero(self):
        self.assertEqual(Place.number_rooms, 0)

    def test_latitude_default_zero_float(self):
        self.assertEqual(Place.latitude, 0.0)

    def test_amenity_ids_default_list(self):
        self.assertIsInstance(Place.amenity_ids, list)

    def test_two_unique_ids(self):
        self.assertNotEqual(Place().id, Place().id)

    def test_in_storage(self):
        p = Place()
        self.assertIn("Place.{}".format(p.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[Place]", str(Place()))


class TestPlaceSave(unittest.TestCase):
    """Tests for Place save method."""

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
        p = Place()
        old = p.updated_at
        p.save()
        self.assertGreater(p.updated_at, old)

    def test_save_creates_file(self):
        p = Place()
        p.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Place().save("unexpected")


class TestPlaceToDict(unittest.TestCase):
    """Tests for Place to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(Place().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(Place().to_dict()["__class__"], "Place")

    def test_has_id(self):
        self.assertIn("id", Place().to_dict())

    def test_dates_are_strings(self):
        d = Place().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            Place().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
