# Python - If/Else, Loops, Functions

# Learning Objectives

## Why is indentation so important in Python?
Indentation is crucial in Python because it determines the structure and flow of your code. Unlike many other programming languages that use braces or semicolons to define blocks of code, Python relies on indentation to indicate code blocks.
## How to use the if/if...else statements?
If-else statements allow you to execute different code blocks based on a condition. They provide a way to make decisions and control the flow of your program.
```python3
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false
```
## How to use comments?
Comments are lines of text in your code that are ignored by the interpreter. They are used to explain your code, make it more readable, and document its functionality.

Single-line comments:

Start with a hash symbol (#).
Everything after the hash symbol on the same line is considered a comment.
```python3
print("Hello, World!") # This is a single line comment
```
Multi-line comments:

Enclosed in triple quotes (''' or """).
Can span multiple lines.
```Python
"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Hello, world!")
```
## How to affect values to variables?
In Python, you assign values to variables using the = operator. The variable name goes on the left side of the operator, and the value you want to assign goes on the right side.

Here are some examples:

Python
### Assigning a number to a variable
x = 10

### Assigning a string to a variable
name = "Alice"

### Assigning a floating-point number to a variable
pi = 3.14159

### Assigning a boolean value to a variable
is_true = True

## How to use the while and for loops?
A while loop repeatedly executes a block of code as long as a specified condition remains true
### Syntax:
```python3
while condition:
    # Code to be executed
```
### Example:
```python3
count = 0
while count < 5:
    print("Count: {}".format(count))
    count += 1
```
## How to use the break and continues statements?
### Break Statement:

The break statement is used to terminate a loop prematurely.
When encountered within a loop, it immediately exits the loop, and the execution continues with the next statement outside the loop.

### Continue Statement:

The continue statement is used to skip the current iteration of a loop and proceed to the next iteration.
When encountered within a loop, it immediately jumps to the beginning of the next iteration.

## How to use else clauses on loops?
In Python, you can use an else clause with both for and while loops. It provides a way to execute code if the loop completes normally, without being terminated by a break statement.

## What does the "pass" statement do, and when to use it?
The pass statement in Python is a placeholder that does nothing. It's often used when you need a statement for syntactical correctness but don't want to perform any action.
### Example:
```python3
def my_function():
    pass

class Dog:
    pass
```
## How to use range?
The range() function in Python generates a sequence of numbers. It's commonly used in for loops to iterate over a specific range of values.

## What does return a function that does not use any return statement?
In Python, every function returns a value. If you don't explicitly specify a return value using the return statement, the function will automatically return None.

## Scope of 
Scope in Python refers to the region of code within which a variable can be accessed and used. Variables defined within a certain scope are not accessible outside of that scope.

## What's a traceback?
A traceback in Python is a detailed report of the sequence of function calls that led to an exception. When an error occurs, Python generates a traceback to help you identify the exact location and cause of the problem.

## What are the arithmetic operators and how to use them?
Arithmetic operators are used to perform mathematical calculations on numbers. Here are the common arithmetic operators in Python:
```python3
# Addition
result = 5 + 3
print(result)  # Output: 8

# Subtraction
result = 10 - 4
print(result)  # Output: 6

# Multiplication
result = 2 * 6
print(result)  # Output: 12

# Division
result = 15 / 3
print(result)  # Output: 5.0

# Floor division
result = 17 // 3
print(result)  # Output: 5

# Modulus
result = 7 % 2
print(result)  # Output: 1

# Exponentiation
result = 2 ** 3
print(result)  # Output: 8
```
