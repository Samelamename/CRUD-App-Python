-- Table contains details of coffee orders.

CREATE Table orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR (30),
    order_type VARCHAR (30),
    cream BOOLEAN, 
    number_orders INTEGER,
    order_cost  FLOAT

);

INSERT INTO orders (customer_name, order_type, cream, number_orders, order_cost) VALUES ('Jammie Tart', 'Chai Latte', true, 2, 8.0);
INSERT INTO orders (customer_name, order_type, cream, number_orders, order_cost) VALUES ('Dani Rojas', 'Espresso', false, 1, 4.50);
INSERT INTO orders (customer_name, order_type, cream, number_orders, order_cost) VALUES ('Roy Kent', 'Hot Choc', true, 2, 3.50);
