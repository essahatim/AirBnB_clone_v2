#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from typing import Dict, Any


Base = declarative_base()


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None:
        """Instantiation of base model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            self.id = str(uuid.uuid4()) if "id" not in kwargs else kwargs["id"]
            self.created_at = datetime.now() if "created_at" not in kwargs else self.created_at
            self.updated_at = datetime.now() if "updated_at" not in kwargs else self.updated_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def __repr__(self) -> str:
        """Returns a string representation for debugging purposes"""
        return self.__str__()

    def save(self) -> None:
        """Updates the public instance attribute updated_at to the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self) -> Dict[str, Any]:
        """Returns a dictionary representation of the object"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop('_sa_instance_state', None)  # Remove SQLAlchemy-specific state
        return my_dict

    def delete(self) -> None:
        """Deletes the object"""
        models.storage.delete(self)
