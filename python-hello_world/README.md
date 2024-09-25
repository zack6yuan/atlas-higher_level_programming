# 🐍 Python - Hello, World ![image](https://github.com/user-attachments/assets/3b71dd5a-db97-4c30-9b8e-cdc65d670f22)

Welcome to the Python World!

# Learning Objectives

## How to use the Python interpreter?
    1. Open the terminal for macOS, or PowerShell for Windows. 
    2. Navigate to the directory where your python script is located.
    3. Run the Python interpreter
    4. Enter Python code directly into the interpreter.
    The interpreter will execute each line of cods as you type it. 
    5. Exit the Interpreter using the command exit() or quit()
## How to print text and variables using print?
    The print() function in Python is a versatile tool 
    used to display output on the console. It can handle
    both text and variables, which allows you to customize
    and format your output.
## How to use strings?
    Strings are sequences of characters in Python.
    They can be enclosed in:
    single quotes (')
    double quotes (")
    or triple quotes (''' or """).

## What are indexing and slicing in Python?
    Indexing and slicing are fundamental operations in Python for
    accessing elements within sequences like strings, lists, and tuples.
## Indexing 
Access Individual Elements:

Indexing allows you to retrieve a specific element from a sequence based on its position.

Start at 0: The first element in a sequence has an index of 0.

Negative Indexing: You can also access elements from the end using negative indices, where -1 refers to the last element.
```
my_list = [1, 2, 3, 4, 5]

# Access the first element
first_element = my_list[0]  # Output: 1

# Access the last element
last_element = my_list[-1]  # Output: 5
```
## Slicing
Extract Subsequences: 

Slicing extracts a portion of a sequence based on start and stop indices.

Optional Step: You can also specify a step size to skip elements.
```
my_string = "Hello, world!"

# Extract the substring "world"
substring = my_string[7:12]  # Output: 'world'

# Extract every other character
every_other = my_string[::2]  # Output: 'Hlo ol'
```

## What is the official Python coding style and how to check your code with pycodestyle?

    The official Python coding style is defined in the PEP 8 style guide. 
    It provides guidelines for code formatting, naming conventions, and other 
    best practices to improve code readability and maintainability.

    Key Points from PEP 8:

    Indentation: Use 4 spaces for indentation.

    Line Length: Limit lines to 79 characters.

    Blank Lines: Use blank lines to separate logical sections of code.

    Naming Conventions: Use lowercase with underscores for 
    variable and function names (e.g., my_variable). 

    Use PascalCase for class names (e.g., MyClass).

    Comments: Use clear and concise comments to explain complex code.
    
    Checking Your Code with pycodestyle
