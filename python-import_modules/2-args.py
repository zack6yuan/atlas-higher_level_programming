#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("{} arguments: {}".format(0, sys.argv))
    elif len(sys.argv) - 1 == 1:
        print("{} argument: {}".format(1, sys.argv))
    else:
        print("{} arguments: {}".format(len(sys.argv), sys.argv))
