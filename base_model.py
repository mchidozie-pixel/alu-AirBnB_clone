#!/usr/bin/python3
"""
Console module.

Command interpreter for the AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit command using EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
