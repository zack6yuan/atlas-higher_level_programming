#!/usr/bin/python3
""" Module that takes in an argument and lists
all the values that are in the states table """
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Method:
        list all states that are in the states table
    Attributes:
        username = 
        password = 
        database name = 
        state name searched = 
    """
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2]
        db=sys.argv[3],
    ) # connect to MySQL database.
    cursor = db.cursor()
    cursor.execute()