#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json


class FileStorage:
    """Serializes instances to JSON file and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <classname>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        odict = {}
        for key, obj in FileStorage.__objects.items():
            odict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review,
        }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                odict = json.load(f)
            for key, value in odict.items():
                cls_name = value.get("__class__")
                if cls_name in classes:
                    FileStorage.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass
