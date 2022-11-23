#!/usr/bin/python3
"""The base model for AirBnB console project"""

from uuid import uuid4
from datetime import datetime
import models

dateFormat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base model for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize object and check keyword argument"""

        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                kwargs["created_at"], dateFormat)
        else:
            self.created_at = datetime.now()
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                kwargs["updated_at"], dateFormat)
        else:
            self.updated_at = self.created_at
        if "id" in kwargs:
            self.id = kwargs["id"]
        else:
            self.id = str(uuid4())
            models.storage.new(self)

    def __str__(self):
        """BaseModel string

        Returns:
                str: return formatted string
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that update `update_at` of object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method that format created_at,
           updated_at and add new key __class__

        Returns:
            dict: return dict with formatted values
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = __class__.__name__
        new_dict["created_at"] = new_dict["created_at"].strftime(
            dateFormat)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(
            dateFormat)
        return new_dict
