#!/usr/bin/python3
import sys

if __name__ == "__main__":
    digit = len(sys.argv) - 1
    if digit == 0:
        print("{} arguments: {}".format(digit, sys.argv[0]))
    elif digit == 1:
        print("{} argument: {}".format(digit, sys.argv[1:]))
    else:
        print("{} arguments: {}".format(digit, sys.argv[1:]))
