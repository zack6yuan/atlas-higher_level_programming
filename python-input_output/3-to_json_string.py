#!/usr/bin/python3
""" Module for "To JSON string" """
import json


def to_json_string(my_obj):
    """ Method: returns the JSON representation of object """
    return (json.dumps(my_obj))
