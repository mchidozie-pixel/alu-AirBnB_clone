#!/usr/bin/python3
"""Unit tests for State."""
import unittest
import os
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestStateInstantiation(unittest.TestCase):
    """Tests for State instantiation."""

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
        self.assertIsInstance(State(), State)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(State(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(State().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_name_is_class_attr(self):
        self.assertIn("name", State.__dict__)

    def test_name_default_empty_str(self):
        self.assertEqual(State.name, "")

    def test_two_unique_ids(self):
        self.assertNotEqual(State().id, State().id)

    def test_in_storage(self):
        s = State()
        self.assertIn("State.{}".format(s.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[State]", str(State()))


class TestStateSave(unittest.TestCase):
    """Tests for State save method."""

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
        s = State()
        old = s.updated_at
        s.save()
        self.assertGreater(s.updated_at, old)

    def test_save_creates_file(self):
        s = State()
        s.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            State().save("unexpected")


class TestStateToDict(unittest.TestCase):
    """Tests for State to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(State().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(State().to_dict()["__class__"], "State")

    def test_has_id(self):
        self.assertIn("id", State().to_dict())

    def test_dates_are_strings(self):
        d = State().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            State().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
