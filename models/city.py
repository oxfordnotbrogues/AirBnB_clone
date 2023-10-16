#!/usr/bin/python3
"""Defines the city class."""
import sys
sys.path.append("../")
from models.base_model import BaseModel



class City(BaseModel):
    """Represent a city.

    Attributes:
    state_id (str): the state id
    name (str): the name of the city.
    """

    state_id = ""
    name = ""
