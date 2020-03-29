#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    tables = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

    cur = tables.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%' ORDER BY id ASC")
    for a in cur:
        print("{}".format(a))
    cur.close()
    tables.close()
