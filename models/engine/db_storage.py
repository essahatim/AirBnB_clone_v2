#!/usr/bin/python3
"""This module defines a class for managing SQL Alchemy database storage"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of AirBnB models using SQL Alchemy"""

    def __init__(self):
        """Initialize DBStorage class"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects or filtered by class"""
        dictionary = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
        else:
            classes = [State, City, User, Place, Review, Amenity]
            query = [self.__session.query(cls) for cls in classes]
            query = [elem for sublist in query for elem in sublist]

        for elem in query:
            key = "{}.{}".format(type(elem).__name__, elem.id)
            dictionary[key] = elem
        return dictionary

    def new(self, obj):
        """Adds a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes to the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configures the session"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
