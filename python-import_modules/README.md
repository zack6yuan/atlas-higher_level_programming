# 🐍 Python - Import & Modules
# Learning Objectives
## How to use imported functions
1. Import the module:

Use the import keyword to import the module containing the function you want to use.
```Python
import module_name
```

Replace module_name with the actual name of the module. For example, to import the math module, you would use:

```Python
import math
```

2. Use the function:

Once you've imported the module, you can use its functions by calling them with the appropriate arguments.
```Python
result = math.sqrt(4)
print(result)  # Output: 2.0
```

In this example, we're importing the math module and using its sqrt() function to calculate the square root of 4.

## How to create a module
A module in Python is a Python file containing Python definitions and statements. It can define functions, classes, and variables. To create a module, simply create a new Python file with a .py extension.

Example:

Create a new file: Let's create a file named my_module.py.

Define functions, classes, and variables: Inside the file, write your Python code. For example:

```Python
def greet(name):
    print("Hello, " + name + "!")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")
```
Save the file: Save the file as my_module.py.

## How to use the built-in function dir()
The dir() function in Python is used to get a list of valid attributes (including methods) of an object. It can be used on any object, including modules, classes, instances, and even built-in types like int, str, and list.

## How to prevent code in your script from being executed when imported
1. Using the if __name__ == "__main__": Guard:

This is the most common and recommended approach. Place the code you want to execute only when the module is run directly, not when it's imported, within this conditional block:

```Python
if __name__ == "__main__":
    # Code to be executed only when the module is run directly
```

The __name__ variable is a built-in variable that holds the name of the current module. When a module is run directly, its __name__ attribute is set to "__main__". If the module is imported, __name__ will be set to the name of the module.
## How to use command line arguments with your Python programs
Command line arguments are values passed to a Python script when it's executed from the command line. They can be used to provide input data, configure the script's behavior, or customize its output.

Using the sys module:

The sys module provides access to system-specific parameters and functions. To use command line arguments, you can import the sys module and access the argv attribute, which is a list containing the command-line arguments.
