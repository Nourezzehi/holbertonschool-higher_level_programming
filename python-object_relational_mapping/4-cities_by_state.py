#!/usr/bin/python3
"""list cities from databases"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    connects to a MySQL server and lists all cities
        from the database hbtn_0e_0_usa
    """

    username, password, database = sys.argv[1:4]

    """connect to my database"""
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306)

    """Create a cursor object"""
    cur = db.cursor()

    """exeute SQL Query"""
    cur.execute("SELECT * FROM cities ORDER By id")

    """fetch Query results"""
    results = cur.fetchall()

    for result in results:
        print(result)
