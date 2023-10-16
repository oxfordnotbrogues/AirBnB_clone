#!/usr/bin/python3
"""Defines the review class"""
import sys
sys.path.append("../")
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.

    Attributes:
    place_id (str): the place id
    user_id (str): the user id
    text (str): the text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
