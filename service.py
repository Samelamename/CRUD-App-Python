# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data
# Not a complete function, but a suggestion of what to do
from db import selectQuery, database


def readAllData(dbName, tableName):
    # Create a database instance
    db = database(dbName)
    # Execute the SELECT query
    query = f"SELECT * FROM {tableName}"
    result = selectQuery(db, query)
    # Close the database connection
    db.close()
    return result
