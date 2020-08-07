#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    query = "SELECT * FROM states ORDER BY id ASC".format(name)

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
