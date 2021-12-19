#!/usr/bin/python3
"""script to print out names start with N from db
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    da = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = da.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    db_rows = cur.fetchall()
    for row in db_rows:
        print("{}".format(row))
    cur.close()
    da.close()
