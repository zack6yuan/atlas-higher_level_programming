#!/usr/bin/python3
""" Module that prints a list of type "int"'s in ascending order """


class MyList(list):
    """ class "MyList, inherits from "list" """
        def print_sorted(self):
            """ Method: prints ascending list of type "int"'s """
            print(sorted(self))
