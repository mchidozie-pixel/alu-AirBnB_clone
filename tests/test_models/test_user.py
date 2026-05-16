#!/usr/bin/python3
"""Unit tests for User."""
import unittest
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUserInstantiation(unittest.TestCase):
    """Tests for User instantiation."""

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
        self.assertIsInstance(User(), User)

    def test_is_subclass_of_base_model(self):
        self.assertIsInstance(User(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(User().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_email_is_class_attr(self):
        self.assertIn("email", User.__dict__)

    def test_password_is_class_attr(self):
        self.assertIn("password", User.__dict__)

    def test_first_name_is_class_attr(self):
        self.assertIn("first_name", User.__dict__)

    def test_last_name_is_class_attr(self):
        self.assertIn("last_name", User.__dict__)

    def test_email_default_empty_str(self):
        self.assertEqual(User.email, "")

    def test_password_default_empty_str(self):
        self.assertEqual(User.password, "")

    def test_first_name_default_empty_str(self):
        self.assertEqual(User.first_name, "")

    def test_last_name_default_empty_str(self):
        self.assertEqual(User.last_name, "")

    def test_two_unique_ids(self):
        self.assertNotEqual(User().id, User().id)

    def test_in_storage(self):
        u = User()
        self.assertIn("User.{}".format(u.id), storage.all())

    def test_str_contains_class_name(self):
        self.assertIn("[User]", str(User()))


class TestUserSave(unittest.TestCase):
    """Tests for User save method."""

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
        u = User()
        old = u.updated_at
        u.save()
        self.assertGreater(u.updated_at, old)

    def test_save_creates_file(self):
        u = User()
        u.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        u = User()
        with self.assertRaises(TypeError):
            u.save("unexpected")


class TestUserToDict(unittest.TestCase):
    """Tests for User to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(User().to_dict(), dict)

    def test_class_name_correct(self):
        self.assertEqual(User().to_dict()["__class__"], "User")

    def test_has_id(self):
        self.assertIn("id", User().to_dict())

    def test_dates_are_strings(self):
        d = User().to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        with self.assertRaises(TypeError):
            User().to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
