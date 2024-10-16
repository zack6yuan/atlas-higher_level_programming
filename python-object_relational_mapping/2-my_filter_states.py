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
        username = first argument
        password = second argument
        database name = third argument
        state name searched = fourth argument
    """
    db = MySQLdb.connect (
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        state_name=sys.argv[4]
    )  # connect to MySQL database.
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)