#!/usr/bin/python3
"""script to get state name and filter
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    da = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = da.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name='{}' ORDER BY id ASC".format(argv[4]))
    db_rows = cur.fetchall()
    for row in db_rows:
        print(row)
    cur.close()
    da.close()
