#!/usr/bin/python3
""" Module that defines class "Base" """
import json


class Base:
    """ Method: initialize "Base" class """
    __nb_objects = 0  # PRVIA (Base Object Counter)

    def __init__(self, id=None):
        """ Method: check id status and assign accordingly """
        if id is not None:
            self.id = id  # Assign "id"
        else:
            Base.__nb_objects += 1  # Increment object counter
            self.id = Base.__nb_objects  # Assign "id" with new value

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method: returns the JSON string
        representation of "list_dictionaries" """
        if (list_dictionaries) is None or (list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    def save_to_file(cls, list_objs):
        """ Method: writes the JSON representation
        of "list_obj"s" to a file"""
        file = "{}.json".format(cls.__name)
            with open(file, "w") as jsonfile:
        if (list_objs) is None:
            jsonfile.write("[]")

    def create(cls, **dictionary):
        """ Method: returns an instance
        with all attributes already set """
        if cls.__name == "Rectangle":
            instance = cls(1, 1)
        if cls.__name = "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return (instance)
