# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3

def setupConn(db_name):
    conn = sqlite3.connect(db_name)
    return conn
