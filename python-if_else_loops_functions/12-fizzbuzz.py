#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        elif i % 3 and i % 5:
            print(f"FizzBuzz")
