#!/usr/bin/python3
"""The base model for AirBnB console project"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base model for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize object and check keyword argument"""

        self.id = kwargs["id"] if "id" in kwargs else str(uuid4())
        self.created_at = datetime.strptime(
            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f") \
            if "created_at" in kwargs else datetime.now()
        self.updated_at = datetime.strptime(
            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f") \
            if "updated_at" in kwargs else datetime.now()

    def __str__(self):
        """BaseModel string

        Returns:
                str: return formatted string
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that update `update_at` of object
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """method that format created_at,
           updated_at and add new key __class__

        Returns:
            dict: return dict with formatted values
        """
        new_dict = self.__dict__
        new_dict["__class__"] = "BaseModel"
        new_dict["created_at"] = new_dict["created_at"].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        new_dict["updated_at"] = new_dict["updated_at"].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        return new_dict
