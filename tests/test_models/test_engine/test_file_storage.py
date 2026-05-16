#!/usr/bin/python3
"""Unit tests for FileStorage."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_instantiates(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_storage_is_file_storage(self):
        self.assertIsInstance(storage, FileStorage)

    def test_file_path_is_str(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_is_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


class TestFileStorageAll(unittest.TestCase):
    """Tests for FileStorage all() method."""

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

    def test_all_returns_dict(self):
        self.assertIsInstance(storage.all(), dict)

    def test_all_with_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.all("unexpected")


class TestFileStorageNew(unittest.TestCase):
    """Tests for FileStorage new() method."""

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

    def test_new_adds_base_model(self):
        bm = BaseModel()
        storage.new(bm)
        self.assertIn("BaseModel.{}".format(bm.id), storage.all())

    def test_new_adds_user(self):
        u = User()
        storage.new(u)
        self.assertIn("User.{}".format(u.id), storage.all())

    def test_new_adds_state(self):
        s = State()
        storage.new(s)
        self.assertIn("State.{}".format(s.id), storage.all())

    def test_new_adds_city(self):
        c = City()
        storage.new(c)
        self.assertIn("City.{}".format(c.id), storage.all())

    def test_new_adds_amenity(self):
        a = Amenity()
        storage.new(a)
        self.assertIn("Amenity.{}".format(a.id), storage.all())

    def test_new_adds_place(self):
        p = Place()
        storage.new(p)
        self.assertIn("Place.{}".format(p.id), storage.all())

    def test_new_adds_review(self):
        r = Review()
        storage.new(r)
        self.assertIn("Review.{}".format(r.id), storage.all())

    def test_new_with_no_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.new()


class TestFileStorageSave(unittest.TestCase):
    """Tests for FileStorage save() method."""

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

    def test_save_creates_file(self):
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_is_valid_json(self):
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)

    def test_save_base_model(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn("BaseModel.{}".format(bm.id), data)

    def test_save_with_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.save("unexpected")


class TestFileStorageReload(unittest.TestCase):
    """Tests for FileStorage reload() method."""

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

    def test_reload_no_file_no_error(self):
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload() raised {} unexpectedly!".format(e))

    def test_reload_with_arg_raises(self):
        with self.assertRaises(TypeError):
            storage.reload("unexpected")

    def test_reload_restores_base_model(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        key = "BaseModel.{}".format(bm.id)
        del FileStorage._FileStorage__objects[key]
        storage.reload()
        self.assertIn(key, storage.all())

    def test_reload_restores_correct_type(self):
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        key = "BaseModel.{}".format(bm.id)
        del FileStorage._FileStorage__objects[key]
        storage.reload()
        self.assertIsInstance(storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()
