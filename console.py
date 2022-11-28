#!/usr/bin/python3
""" A simple console.py that contains the
    entry point of the command interpreter.
"""

import cmd
import json
import re
import models
from models.base_model import BaseModel
from datetime import datetime
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

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            - Usage:
            update <class name> <id> <attribute name> "<attribute value>"
            - Ex:
            $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
            - Only one attribute can be updated at the time"""
        cmd_line = line.split()
        untouchable = ["id", "created_at", "updated_at"]
        objects = models.storage.all()
        if not line:
            print("** class name missing **")
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(cmd_line) < 3:
                print("** attribute name missing **")
            elif len(cmd_line) < 4:
                print("** value missing **")
            elif cmd_line[2] not in untouchable:
                ojb = objects[instance]
                ojb.__dict__[cmd_line[2]] = cmd_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()
        """Updates an instance based on the class
           name and id by adding or updating attribute
        """
        # Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

    def default(self, line):
        """call class model methods with dot parameter
        """
        arg = line.split(".")
        if arg[0] in classes.keys() and len(arg) > 1:
            # show method
            shmtd = re.search(r"^show\(\"(.+)\"\)", arg[1])
            # destroy method
            demtd = re.search(r"^destroy\(\"(.+)\"\)", arg[1])
            # update method
            u_m = re.search(
                r"^update\(\"([\w-]+).*\"([\w-]+).*\"([\w-]+)\"\)", arg[1])
            if arg[1] == "all()":
                self.do_all(arg[0])
            elif arg[1] == "count()":
                self.count(arg[0])
            elif shmtd:
                self.do_show(f"{arg[0]} {shmtd.group(1)}")
            elif demtd:
                self.do_destroy(f"{arg[0]} {demtd.group(1)}")
            elif u_m:
                x = f"{arg[0]} {u_m.group(1)} {u_m.group(2)} {u_m.group(3)}"
                self.do_update(x)
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)

    def count(self, arg):
        all_objs = storage.all()
        count = 0
        for obj_id in all_objs.keys():
            obj_class = obj_id.split(".")
            if obj_class[0] == arg:
                count += 1
        print(count)

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        return True

    def emptyline(self):
        """overridden to not do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
