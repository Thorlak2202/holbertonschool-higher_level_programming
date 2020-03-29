#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    tables = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])

    cur = tables.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from cities \
                JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    for a in cur:
        print("{}".format(a))
    cur.close()
    tables.close()
