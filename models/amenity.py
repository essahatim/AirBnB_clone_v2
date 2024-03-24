#!/usr/bin/python3
"""This module defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity class for representing amenities.

    Attributes:
        name (str): The name of the amenity.
        place_amenities (relationship): Relationship with Place objects.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
