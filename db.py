# # The DB file contains the processes and functions to create our database or connect to it as well as run the initial SQL
# # The DB file should also contain query functions that the Service file can use to read or modify the data
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

#Function that enables reading data
def selectQuery(database,query):
    return database.cursor.execute(query).fetchall()

#Function that enables functions to maninpulate data
def dataQuery(database, query):
    database.cursor.execute(query)
    return True
    
def commitChanges(database):
    database.conn.commit()