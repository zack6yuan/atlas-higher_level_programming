#!/usr/bin/python3
""" Module for "read file" """


def read_file(filename=""):
    """ Method: reads text file + prints to stdout """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
