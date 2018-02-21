#! /usr/local/bin/python3

import psycopg2
import subprocess
connect_pgsql_via_shell = subprocess.run(["psql -h 'localhost' -U 'vidhaikalam' -d 'vidhaikalam'"], stdout=subprocess.PIPE)
print(connect_pgsql_via_shell.stdout)
print('########################')
try:
    conn = psycopg2.connect(database='spc', user='spc', host='localhost', password='spc')
    cur = conn.cursor()

    # show all table in this database
    cur.execute("SELECT id, first_name  from AUTH_USER")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
except:
    print("I am unable to connect to the database")
