#!/usr/bin/python3
"""This module defines the subclass(User) to from (BaseModel)"""
from models.base_model import BaseModel


class User(BaseModel):
    """Subclass(User), represent an users with them informations.

    Public class attributes:
        email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
