#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("{} arguments: {}".format(0, sys.argv))
    elif len(sys.argv) - 1 == 1:
        print("{} argument: {}".format(1, sys.argv[1:]))
    else:
        print("{} arguments: {}".format(len(sys.argv) - 1, sys.argv[1:]))
