#!/usr/bin/python3
"""The user model for AirBnB console project"""

from models.base_model import BaseModel

class User(BaseModel):
	"""A User model for AirBnB clone"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""