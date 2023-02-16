# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data
# Not a complete function, but a suggestion of what to do
from db import *

def createTable(db, sqlFileName):
    # create a tableCreator instance
    creator = tableCreator(db, sqlFileName)
    # create the tables
    creator.create()
    # commit the changes
    db.conn.commit()
    # close the database connection
    db.close()

#Reads All data in table specified. 
def readAllData(db, tableName):
    # Execute the SELECT query
    query = f"SELECT * FROM {tableName}"
    result = selectQuery(db, query)
    # Close the database connection
    return result


#Deletes data from table by ID
def deleteOrderId(db):
    orderID = int(input("What is the ID of the order you would like to delete? "))
    query = f"DELETE FROM orders where order_id = {orderID}"
    dataQuery(db, query)
    return True

def createOrder(db):
    customerName = input("Please enter the name of the customer: ")
    orderType = input("Please enter what they ordered: ")
    creamBool = input("Please enter whether or not cream was added (true/false): ")
    numberOrders = input("Please enter the amount ordered: ")
    orderCost = input("Please enter the total cost of the order: ")
    query = f"INSERT INTO orders (customer_name, order_type, cream, number_orders, order_cost) VALUES ('{customerName}', '{orderType}', {creamBool.lower()}, {numberOrders}, {orderCost});"
    dataQuery(db, query)
    return True
    

#Updates entry in table by ID
def updateOrderNameId(db, id, name):
    query = f"UPDATE orders SET customer_name = '{name}' WHERE order_id = {id}"
    dataQuery(db, query)
    return True
