#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT A.id, A.name, B.name FROM cities A LEFT OUTER JOIN " + "states B ON A.state_id = B.id ORDER BY A.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    db.close()
