#!/usr/bin/python3
""" A simple console.py that contains the
    entry point of the command interpreter.
"""

import cmd
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        "Command to create a model and save to storage\n"
        if len(arg) != 0:
            if arg in classes.keys():
                create_model = classes[arg]()
                create_model.save()
                print(create_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, *args):
        "Command to show model details base on it I.D\n"
        args_list = args[0].split(' ')
        if len(args[0]) != 0:
            if args_list[0] in classes.keys():
                if len(args_list) > 1:
                    # filename = self.__file_path
                    try:
                        objStr = f"{args_list[0]}.{args_list[1]}"
                        with open("file.json", encoding="UTF8") as file:
                            load = json.load(file)
                        if objStr in load:
                            show_object = classes[load[objStr]["__class__"]](
                                **load[objStr])
                            print(show_object)
                        else:
                            print("** no instance found **")
                    except FileNotFoundError:
                        pass
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, *args):
        "Command to deletes an instance based on the class name and id\n"
        args_list = args[0].split(' ')
        if len(args[0]) != 0:
            if args_list[0] in classes.keys():
                if len(args_list) > 1:
                    # filename = self.__file_path
                    try:
                        objStr = f"{args_list[0]}.{args_list[1]}"
                        with open("file.json", encoding="UTF8") as file:
                            load = json.load(file)
                        if objStr in load:
                            with open("file.json", "w",
                                      encoding="UTF8") as file:
                                del load[objStr]
                                json.dump(load, file)
                        else:
                            print("** no instance found **")
                    except FileNotFoundError:
                        pass
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, *args):
        """Prints all string representation of all
           instances based or not on the class name"""
        args_list = args[0].split(' ')
        if len(args_list[0]) > 0:
            all_objs = storage.all()
            list_all_objs = []
            for obj_id in all_objs.keys():
                obj_class = obj_id.split(".")
                if obj_class[0] == args_list[0]:
                    obj = all_objs[obj_id]
                    list_all_objs.append(obj.__str__())
            if len(list_all_objs) > 0:
                print(list_all_objs)
            else:
                print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_all_objs = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                list_all_objs.append(obj.__str__())
            print(list_all_objs)

    def do_update(self, *args):
        """Updates an instance based on the class
           name and id by adding or updating attribute
        """
        # Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        args_list = args[0].split(' ')
        # print(args_list)
        if len(args[0]) != 0:
            if args_list[0] in classes.keys():
                if len(args_list) > 1:
                    # filename = self.__file_path
                    try:
                        objStr = f"{args_list[0]}.{args_list[1]}"
                        with open("file.json", encoding="UTF8") as file:
                            load = json.load(file)
                        if objStr in load:
                            if 2 < len(args_list):
                                if 3 < len(args_list):
                                    with open("file.json",
                                              "w", encoding="UTF8") as file:
                                        load[objStr][args_list[2]
                                                     ] = args_list[3]
                                        json.dump(load, file)
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    except FileNotFoundError:
                        pass
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        sys.exit()

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        sys.exit()

    def emptyline(self):
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
