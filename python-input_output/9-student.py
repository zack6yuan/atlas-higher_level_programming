#!/usr/bin/python3
""" Module for "Student to JSON" """


class Student:
    """ Class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Method: initialize the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method: retrieves a dictionary 
        representation of a "Student" instance """
        return (self.__dict__)
