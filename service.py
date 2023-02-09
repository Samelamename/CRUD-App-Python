# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data
# Not a complete function, but a suggestion of what to do
from db import selectQuery, dataQuery, commitChanges, database


#Reads All data in table specified. 
def readAllData(dbName, tableName):
    # Create a database instance
    db = database(dbName)
    # Create a cursor to interact with the database
    # cursor = conn.cursor()
    # Execute the SELECT query
    query = f"SELECT * FROM {tableName}"
    result = selectQuery(db, query)
    # Close the database connection
    db.close()
    return result
#deletes data from table by ID
def deleteOrderId(dbName, id):
    db = database(dbName)
    query = f"DELETE FROM orders where order_id = {id}"
    return dataQuery(db, query)

def updateOrderNameId(dbName, id, name):
    db = database(dbName)
    query = f"UPDATE orders SET order_name = '{name}' WHERE order_id = {id}"
    dataQuery(db, query)
    commitChanges(db)
    db.close()
    return True
