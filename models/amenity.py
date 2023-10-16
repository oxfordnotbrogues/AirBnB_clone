#!/usr/bin/python3
""" Defines the amenity class"""
import sys
sys.path.append("../")
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.

    Attributes:
      name (str): The name of the amenity
    """
    name = ""
