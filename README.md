# Project - AirBnB Clone
![image](https://github.com/savvyh/holbertonschool-AirBnB_clone/assets/139894873/d37a2a69-89f4-4109-b02b-ed487565684a)

## General 🏠
The first step of the team project "AirBnB clone" is to write a command interpreter to manage AirBnB objects.

![image](https://github.com/savvyh/holbertonschool-AirBnB_clone/assets/139894873/daa08960-153e-4f4d-9f3d-ace5996bba8b)

Here are the key concept of this first step of this project :
* Put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances.
* Create a simple flow of serialization/deserialization: `Instance <-> Dictionary <-> JSON string <-> file`.
* Create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`.
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all classes and storage engine.

## Requirements ♟️
#### Python Script : 

* We are not allowed to import module.
* Respect the pycodestyle.
* All files must be executable.
* Use `#!/usr/bin/python3`.
* The shell should work like this in interactive mode but also in non-interactive mode.

#### Python Unit Test : 

* All test files should be inside a folder tests.
* All test files should be text files (extension: .txt).
* All tests should be executed by using this command: `python3 -m doctest ./tests/*`.
* All modules and functions should have a documentation.
* Use the `Unittest` mmodule.

## Before to start 📖
- How to create a Python package: Organize the code into modules and put them in a directory with a special file called __init__.py.
- How to create a command interpreter in Python using the cmd module: Subclass `cmd.Cmd`, define the command as methods with names starting with `do_`, and then use the `cmdloop()` method to start the command interpreter.
- What is Unit testing and how to implement it in a large project: Unit testing is a way to test individual units or components of a software. In Python, we can use the built-in `unittest` module and execute unit tests for various parts of your code.
- How to serialize and deserialize a Class: We can use the `pickle` module in Python to serialize (convert objects into a byte stream) and deserialize (convert the byte stream back into objects) a class instance.
- How to write and read a JSON file: Use the json module in Python. To write, use `json.dump(data, file)` or `json.dumps(data)` to get a string. To read, use `json.load(file)` or `json.loads(string)`.
- How to manage datetime: Use the `datetime` module in Python. We can create datetime objects, perform arithmetic operations, format dates, and much more.
- What is an UUID: UUID, or Universally Unique Identifiers, are used to generate unique and globally unambiguous identifiers in computer systems. They ensure uniqueness of objects and data, which is crucial in distributed environments, databases, web applications, etc.
- What is `*args` and how to use it: `*args` is used in function definitions to pass a variable number of positional arguments. Inside the function, `*args` is a tuple containing all the arguments passed.
- What is `**kargs` and how to use it: `**kargs` is used in function definitions to pass a variable number of keyword arguments. Inside the function, `**kargs` is a dictionary containing all the keyword arguments passed.
- How to handle named arguments in a function: We can define functions with named arguments, also known as keyword arguments. These are specified in the function definition like `def my_function(arg1, arg2=default_value)`, where `arg2` has a default value. When calling the function, you can provide arguments by name like `my_function(arg1=value1, arg2=value2)`.

## The command interpreter 🔄
