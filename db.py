# # The DB file contains the processes and functions to create our database or connect to it as well as run the initial SQL
# # The DB file should also contain query functions that the Service file can use to read or modify the data


# Creating a connection object, by running the connect() function
# def setupConn():
#     conn = sql.connect("coffeeOrder")
#     return conn

# def cursor():
#     cursor = setupConn().cursor()
#     return cursor
import sqlite3 as sql
# conn = sql.connect("coffeeOrder")
# cursor = conn.cursor()
# def creatingTable():
#     sqlFile = open("coffeeOrder.sql")
#     sqlString = sqlFile.read()
#     # print(sqlString)
#     # Running our sql command using our cursor
#     cursor.executescript(sqlString)

# creatingTable()

# print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()) 



# class database:
#     _instance = None

#     def _New__(cls):
#         if cls._instance is None:
#             cls._instance = super()._New__(cls)
#             cls.Conn = sql.connect("coffee")
#             cls.Cursor = cls.Conn.cursor()
#         return cls._instance

#     def getConn(self):
#         return self.Conn

#     def getCursor(self):
#         return self.Cursor

# def setupConn():
#     return database().getConn()

# def setupCursor():
#     return database().getCursor()

# def creatingTable():
#     sqlFile = open("coffeeOrder.sql")
#     sqlString = sqlFile.read()
#     setupCursor().executescript(sqlString)

# def select_query(query):
#     return setupCursor().execute(query).fetchall()

# def data_query(query):
#     setupCursor().execute(query)
#     return True

# def commitChanges():
#     setupConn().commit()



# 
# creatingTable()


import sqlite3 as sql

class database:
    def __init__(self, dbName):
        # create a connection to the SQLite database
        self.conn = sql.connect(dbName)
        # create a cursor to interact with the database
        self.cursor = self.conn.cursor()

    def close(self):
        # close the database connection
        self.conn.close()



class tableCreator:
    def __init__(self, database, sqlFileName):
        # take a database instance and a SQL file name as arguments
        self.database = database
        self.sqlFileName = sqlFileName

    def create(self):
        # read the SQL file
        with open(self.sqlFileName) as f:
            sqlString = f.read()
        # execute the SQL commands to create the tables
        self.database.cursor.executescript(sqlString)

def createTable(dbName, sqlFileName):
    # create a database instance
    db = database(dbName)
    # create a tableCreator instance
    creator = tableCreator(db, sqlFileName)
    # create the tables
    creator.create()
    # commit the changes
    db.conn.commit()
    # close the database connection
    db.close()

# call the createTable function with the database name and SQL file name
# createTable("coffeeOrder", "coffeeOrder.sql")


def selectQuery(database,query):
    return database.cursor.execute(query).fetchall()




