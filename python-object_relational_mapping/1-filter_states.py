#!/usr/bin/python3
""" Module that lists all states with a name starting with "N"
From the database "hbtn_0e_0_usa" """
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Method:
        list all states with a name starting with "N" (uppercase)
        from the database "hbtn_0e_0_usa"
    Attributes:
        username = first argument
        password = second argument
        database name = third argument
    """
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )  # connect to MySQL database.
    cursor = db.cursor()  # create cursor object
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
