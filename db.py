# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sql
# Creating a connection object, by running the connect() function
def setup_conn():
    conn = sql.connect("coffee_order")
    return conn

def cursor():
    cursor = setup_conn().cursor()
    return cursor


def creatingTable():
    sql_file = open("cinema.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)