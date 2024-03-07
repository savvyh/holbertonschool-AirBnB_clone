#!/usr/bin/python3
"""This module defines the subclass(City) to from (BaseModel)"""
from models.base_model import BaseModel


class City(BaseModel):
    """Subclass(City), represent a city with them informations.

    Public class attributes:
        state_id(str): Id of state to city_name.
        name(str): Empty string.
    """
    state_id = ""
    name = ""
