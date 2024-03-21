#!/usr/bin/python3
"""This module defines a class for managing file storage in AirBnB"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances"""

    def __init__(self):
        """Initialize FileStorage class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or filtered by class"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects to a JSON file"""
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                self.__objects = {k: eval(v["__class__"])(**v)
                                  for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Reloads objects from JSON file"""
        self.reload()

