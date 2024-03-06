#!/usr/bin/python3
"""This module defines the subclass(Review) to from (BaseModel)"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Subclass(Review), represent a review with them informations.

    Public class attributes:
        place_id(str): Place id.
        user_id(str): User id.
        text(str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
