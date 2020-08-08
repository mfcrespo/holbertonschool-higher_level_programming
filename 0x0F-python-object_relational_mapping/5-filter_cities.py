#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities INNER JOIN states \
                 ON cities.states_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (state_name, ))
    rows = cur.fetchall()
    """for row in rows:"""
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
