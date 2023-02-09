# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data
# Not a complete function, but a suggestion of what to do
from db import selectQuery, dataQuery, commitChanges, database, initializeDb


#Reads All data in table specified. 
def readAllData(db, tableName):
    # Create a database instance
    # Create a cursor to interact with the database
    # cursor = conn.cursor()
    # Execute the SELECT query
    query = f"SELECT * FROM {tableName}"
    result = selectQuery(db, query)
    # Close the database connection
    return result


#Deletes data from table by ID
def deleteOrderId(db, id):
    query = f"DELETE FROM orders where order_id = {id}"
    commitChanges(db)
    dataQuery(db, query)
    return True


#Updates entry in table by ID
def updateOrderNameId(db, id, name):
    query = f"UPDATE orders SET order_name = '{name}' WHERE order_id = {id}"
    dataQuery(db, query)
    commitChanges(db)
    return True
