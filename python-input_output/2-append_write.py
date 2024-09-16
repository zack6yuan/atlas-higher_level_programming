#!/usr/bin/python3
""" Module for "Append to file" """


def append_write(filename="", text=""):
    """ Method: appends string at the end of text file
    and returns the number of characters added """
    with open(filename, "a", endoing="utf8") as file:
        return (file.write(text))
