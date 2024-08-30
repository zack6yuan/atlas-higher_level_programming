#!/usr/bin/python3
import sys
if __name__ == "__main__":
    digit = len(sys.argv) - 1
    if digit == 0:
        print("{}".format("0 arguments."))
    elif digit == 1:
        print("{} argument: ".format(digit))
    else:
        print("{} arguments: ".format(digit))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
