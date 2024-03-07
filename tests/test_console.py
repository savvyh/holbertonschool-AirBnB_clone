#!usr/bin/python3
""" Unittest file for the console.py"""

from console import HBNBCommand
import unittest
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """Unittest to test the console"""

    def setUp(self):
        """Setup for each test"""
        self.cmd = HBNBCommand()

    def test_quit(self):
        """Test the command quit to exit the program"""
        with self.assertRaises(SystemExit):
            self.cmd.do_quit(None)

    def test_EOF(self):
        """Test the command EOF to exit the program"""
        with self.assertRaises(SystemExit):
            self.cmd.do_EOF(None)

    def test_emptyline(self):
        """Test if there is an empty line and do nothing"""
        with StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            self.cmd.emptyline()
            output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
