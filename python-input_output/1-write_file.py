#!/usr/bin/python3
""" Module for "write to a file" """


def read_file(filename=""):
    """ Method: writes to a text file + returns # of chars written """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
