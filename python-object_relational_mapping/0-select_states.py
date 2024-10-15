#!/usr/bin/python3
""" Module that lists all the states from the database "hbtn_0e_0_usa" """
import MySQLdb
import sys

if __name__ == "__main__":
    """
        Method:
            list all states from database
        Attributes:
            username = first argument
            password = second argument
            db (database) = third argument
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
        )  # connect to MySQL database.
    cursor = db.cursor()  # create cursor object.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
