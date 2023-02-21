# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user
from src.service import *
db = initializeDb("coffeeOrder")
# createTable(db, "coffeeOrder.sql")
def runApp():
    print(
        f"""
        Welcome to the Olaad Cafe,
        Here is all the orders in the database currently:

{readAllData(db)}

        What would you like to do?
        1. Create an order
        2. Read an order
        3. Read all Orders
        4. Update an order
        5. Delete an order
        6. Exit
        """
    )
    
    running = True

    while running:
        choice = int(input("Please select a choice using a number: "))
        if choice == 1:
            createOrder(db)
            commitChanges(db)
        elif choice == 2:
            print(readByName(db))
        elif choice == 3:
            print(readAllData(db))
        elif choice == 4:
            idNum = input("Please enter the order ID you would like to update: ")
            customerName = input("Please enter the name you would like to update the order with: ")
            updateOrderNameId(db, idNum, customerName)
        elif choice == 5:
            deleteOrderId(db)
        elif choice == 6:
            running = False
        else: 
            print("Incorrect choice.. try again..")


        endChoice = input("Do you want to query more data Y / N: ")
        if endChoice.upper() == "N":
                running = False
        
runApp()

db.close()