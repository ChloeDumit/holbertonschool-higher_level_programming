#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    temp = []

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT A.name FROM cities A LEFT JOIN states B \
                ON A.state_id = B.id WHERE B.name = %s \
                ORDER BY A.id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        temp.append(row[0])
    print(", ".join(temp))

    cur.close()
    db.close()
