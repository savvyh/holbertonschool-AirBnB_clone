#!/usr/bin/python3
"""This module defines the subclass(State) to from (BaseModel)"""
from models.base_model import BaseModel


class State(BaseModel):
    """Subclass(State), represent a state with them informations.

    Public class attributes:
        name(str): Empty string.
    """
    name = ""
