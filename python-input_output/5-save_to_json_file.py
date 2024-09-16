#!/usr/bin/python3
""" Module for "Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ Method: writes ab object to a text
    file using a JSON representation """
    with open(filename, "w") as file:
        return (json.dump(my_obj, file))
    