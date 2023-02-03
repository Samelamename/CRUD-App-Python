# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do
def read_by_id(id):
    order_data = db.query(id)
    order = order(order_data) 
    
def create_order(drink_name, customer, size, quantity):
    order = Order(drink_name, customer..)
