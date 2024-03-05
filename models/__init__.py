#!/usr/bin/python3
"""Create unique instance of FileStorage() to be used in our application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
