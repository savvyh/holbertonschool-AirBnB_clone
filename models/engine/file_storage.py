#!/usr/bin/python3
"""This module defines the class (FileStorage)"""
from json import dump, load
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """This class is used to serialized and deserializated an object

    Private class attributes:
        __file_path(str): Path to the JSON file.
        __objects(dict): Empty dict. Used to store all objects.

    Public instance methods:
        all(): Return the dictionnary (__objects).
        new(): Set the new OBJ in (__objects) like this format:
                (<obj class_name>.<id>)
        save(): Serialize (__objects) to JSON file.
        reload(): Deserialize JSON file to (__objects).
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionnary (__objects)."""
        return FileStorage.__objects

    def new(self, obj):
        """Set the new OBJ in (__objects) like this format:
                (<obj class_name>.<id>)

        Args:
            obj(dict): Dict representation of an object.
        """
        name = obj.__class__.__name__
        key = "{}.{}".format(name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save all objects contains in (__objetcs) to a file."""
        buff__obj = FileStorage.__objects
        __obj_to_dict = {}
        for (key, dic) in buff__obj.items():
            __obj_to_dict[key] = dic.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            dump(__obj_to_dict, file)

    def reload(self):
        """Recreate each object storage in the JSON file, if it exist"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                obj = load(file)
                for (key, value) in obj.items():
                    _BaseModel = globals()[value['__class__']]
                    instance = _BaseModel(**value)
                    FileStorage.__objects[key] = instance
