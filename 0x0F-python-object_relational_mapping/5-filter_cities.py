#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    da = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = da.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON states.id=cities.state_id\
                WHERE states.name='{}' ORDER BY cities.id ASC".format(argv[4]))
    db_rows = cur.fetchall()
    strr = ''
    count = 0
    for row in db_rows:
        value = ", ".join(row)
        if (count == 0):
            strr += value
        else:
            strr += ', ' + value
        count += 1
    print(strr)
    cur.close()
    da.close()
