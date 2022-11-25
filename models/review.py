#!/usr/bin/python3
"""The review model for AirBnB console project"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A review model for AirBnB clone"""
    place_id = ""
    user_id = ""
    text = ""
