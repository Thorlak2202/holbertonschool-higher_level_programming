#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        tables = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])

        cur = tables.cursor()
        cur.execute("SELECT * from states WHERE name='{:s}'\
                    ORDER BY id ASC".format(argv[4]))
        for row in cur:
            print("{}".format(row))
        cur.close()
        tables.close()
