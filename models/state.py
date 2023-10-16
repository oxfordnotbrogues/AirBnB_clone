#!/usr/bin/python3
"""Defines the state class"""
import sys
sys.path.append("../")
from models.base_model import BaseModel


class State(BaseModel):
    """Representing a state.

    Attributes:
    name (str): the name of the state
    """

    name = ""
