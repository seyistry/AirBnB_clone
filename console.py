#!/usr/bin/python3
""" A simple console.py that contains the
    entry point of the command interpreter.
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """AirBnB command interprter
    """
    prompt = '(hbnb) '

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
