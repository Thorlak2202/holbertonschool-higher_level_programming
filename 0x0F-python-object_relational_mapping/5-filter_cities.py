#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    tables = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])

    cur = tables.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON states.id = cities.state_id \
                WHERE states.name='{:s}' \
                ORDER BY cities.id ASC".format(argv[4]))
    cities = []
    for a in cur:
        cities.append(a[0])
    print(", ".join(cities))
    cur.close()
    tables.close()
