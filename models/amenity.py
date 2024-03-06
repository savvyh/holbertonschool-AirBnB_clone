#!/usr/bin/python3
"""This module defines the subclass(Amenity) to from (BaseModel)"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Subclass(Amenity), represent a city with them informations.

    Public class attributes:
        name(str): name to amenity. Default empty.
    """
    name = ""
