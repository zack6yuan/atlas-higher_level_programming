#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tail = (abs(number) % 10) if (number >= 0) else -(abs(number) % 10)
if (tail > 5):
    print(f"Last digit of {number} is {tail} and is greater than 5")
elif (tail == 0):
    print(f"Last digit of {number} is {tail} and is 0")
else:
    print(f"Last digit of {number} is {tail} and is less than 6 and not 0")
