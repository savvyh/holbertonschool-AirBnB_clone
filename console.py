#!/usr/bin/env python3
"""
Console that contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Create a class HBNBCommand for the interpreter command
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def empty_line(self):
        """
        Pass and do nothing with an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
