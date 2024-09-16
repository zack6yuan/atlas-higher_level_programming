#!/usr/bin/python3
""" Module that reads a text file + prints to stdout """


def read_file(filename=""):
    """ Method: reads text file + prints to stdout """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
