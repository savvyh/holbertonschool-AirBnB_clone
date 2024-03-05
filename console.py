#!/usr/bin/env python3
"""
Console that contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Create a class HBNBCommand for the interpreter command
    Command interpreter:
        Quit : exit the program
        EOF : exit the program
        Emptyline : do nothing
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Command quit to exit the program.
        """
        raise SystemExit

    def do_EOF(self, arg):
        """
        Command EOF to exit the program.
        """
        print()
        raise SystemExit

    def emptyline(self):
        """
        Pass and do nothing with an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
