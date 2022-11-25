#!/usr/bin/python3
"""a class `FileStorage` that serializes instances to a
   JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """A file storage class in json format
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all object

        Returns:
            obj: return class object
        """
        return self.__objects

    def new(self, obj):
        """method to sets in __objects the obj

        Args:
            obj (_type_): object of base class
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        file_path = self.__file_path
        objectToDict = {}
        for key in self.__objects:
            objectToDict[key] = self.__objects[key].to_dict()
        with open(file_path, "w", encoding='utf8') as fp:
            json.dump(objectToDict, fp)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        filename = self.__file_path
        try:
            with open(filename, encoding="UTF8") as file:
                jsonToObject = json.load(file)
            for key in jsonToObject:
                self.__objects[key] = classes[jsonToObject[key]["__class__"]](
                    **jsonToObject[key])
        except FileNotFoundError:
            pass
