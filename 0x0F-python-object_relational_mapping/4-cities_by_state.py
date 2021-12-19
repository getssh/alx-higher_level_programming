#!/usr/bin/python3
"""script to get values from 2 tables
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    da = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = da.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON cities.state_id=states.id\
                ORDER BY cities.id ASC")
    db_rows = cur.fetchall()
    for row in db_rows:
        print(row)
    cur.close()
    da.close()
