#!/usr/bin/python3
""" Module for "Create object from a JSON file" """
import json


def load_from_json_file(filename):
    """" Method: creates an object from a JSON file """
    with open(filename) as file:
        return (json.load(file))
