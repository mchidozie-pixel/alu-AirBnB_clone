#!/usr/bin/python3
"""Unit tests for BaseModel."""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModelInstantiation(unittest.TestCase):
    """Tests for BaseModel instantiation."""

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
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_id_is_str(self):
        self.assertIsInstance(BaseModel().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_two_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_str_contains_class_name(self):
        self.assertIn("BaseModel", str(BaseModel()))

    def test_str_contains_id(self):
        bm = BaseModel()
        self.assertIn(bm.id, str(bm))

    def test_kwargs_instantiation(self):
        dt = datetime.utcnow()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dt)

    def test_class_key_not_in_dict(self):
        bm = BaseModel()
        self.assertNotIn("__class__", bm.__dict__)

    def test_new_instance_in_storage(self):
        bm = BaseModel()
        self.assertIn("BaseModel.{}".format(bm.id), storage.all())


class TestBaseModelSave(unittest.TestCase):
    """Tests for BaseModel save method."""

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
        bm = BaseModel()
        old = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, old)

    def test_save_creates_file(self):
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg_raises(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save("unexpected")


class TestBaseModelToDict(unittest.TestCase):
    """Tests for BaseModel to_dict method."""

    def test_returns_dict(self):
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_has_correct_keys(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_class_name_is_correct(self):
        self.assertEqual(BaseModel().to_dict()["__class__"], "BaseModel")

    def test_dates_are_strings(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_to_dict_with_arg_raises(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict("unexpected")


if __name__ == "__main__":
    unittest.main()
