#!/usr/bin/python3
""" Module for "write to a file" """


def write_file(filename="", text=""):
    """ Method: writes to a text file + returns # of chars written """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
