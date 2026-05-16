#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all AirBnB clone models."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        from models import storage
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, time_fmt)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at and save to storage."""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Return dictionary representation."""
        d = self.__dict__.copy()
        d["__class__"] = type(self).__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
