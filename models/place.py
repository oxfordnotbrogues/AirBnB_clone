#!/usr/bin/python3
"""Defines the place class."""
import sys
sys.path.append("../")
from models.base_model import BaseModel


class Place(BaseModel):
    """Representing a place.

    Attributes:
    city_id (str): the city id
    user_id (str): the user id
    name (str): the name of the place
    description (str): the description of the place
    number_rooms (int): the number of rooms of the place
    number_bathrooms (int): the number of  bathrooms in the place
    max_guest (int): the maximum number of guests of the place
    price_by_night i(int): the price by night of the place
    lattitude (float): the lattitude of the place
    longitude (float): the longitude of the place
    amenity_ids (list): a list of amenity ids
    """
    city_id = ""
    use_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
