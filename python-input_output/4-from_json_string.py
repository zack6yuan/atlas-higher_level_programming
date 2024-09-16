#!/usr/bin/python3
""" Module for "From JSON string to Object" """
import json


def from_json_string(my_str):
    """ Method: returns an JSON represented object """
    return (json.loads(my_str))
