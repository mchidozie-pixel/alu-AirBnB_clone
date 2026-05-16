#!/usr/bin/python3
"""This module instantiates the storage object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
