#!/usr/bin/python3
"""
BaseModel module.

Defines the BaseModel class used for all objects.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models.

    Attributes:
        id (str): unique identifier
        created_at (datetime): creation timestamp
        updated_at (datetime): update timestamp
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            self.id = kwargs.get("id")
            self.created_at = datetime.fromisoformat(
                kwargs.get("created_at")
            )
            self.updated_at = datetime.fromisoformat(
                kwargs.get("updated_at")
            )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert instance to dictionary.

        Returns:
            dict: dictionary representation
        """
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = (
            self.created_at.isoformat()
        )
        instance_dict["updated_at"] = (
            self.updated_at.isoformat()
        )
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict

    def __str__(self):
        """Return string representation."""
        return (
            f"[{self.__class__.__name__}] "
            f"({self.id}) {self.__dict__}"
        )
