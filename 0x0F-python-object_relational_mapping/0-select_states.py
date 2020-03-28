#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    tables = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = tables.cursor()
    cur.execute("SELECT * from states ORDER BY id ASC")
    for row in cur:
        print("{}".format(row))
    cur.close()
    tables.close()