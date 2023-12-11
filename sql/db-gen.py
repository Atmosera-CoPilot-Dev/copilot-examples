import sqlite3
from faker import Faker
import random

fake = Faker()

# Connect to SQLite database in the same directory
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Create tables
c.execute('''
    CREATE TABLE User (
        customer_id INTEGER PRIMARY KEY,
        email_address TEXT,
        first_name TEXT,
        last_name TEXT
    )
''')

c.execute('''
    CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT
    )
''')

c.execute('''
    CREATE TABLE Orders (
        customer_id INTEGER,
        purchase_date TEXT,
        purchase_amt_dollars REAL,
        product_id INTEGER,
        FOREIGN KEY(customer_id) REFERENCES User(customer_id),
        FOREIGN KEY(product_id) REFERENCES Products(product_id)
    )
''')

# Generate data for User
for customer_id in range(1, 21):
    email_address = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name() 
    c.execute("INSERT INTO User VALUES (?, ?, ?, ?)", (customer_id, email_address, first_name, last_name))

# Generate data for Products
product_ids = []
for _ in range(20):
    product_id = fake.unique.random_number(digits=5)
    product_ids.append(product_id)
    product_name = fake.bs()
    c.execute("INSERT INTO Products VALUES (?, ?)", (product_id, product_name))

# Generate data for Orders
for _ in range(50):
    customer_id = random.randint(1, 20)  # Use customer_ids from 1 to 20
    purchase_date = fake.date_time_this_year().isoformat()
    purchase_amt_dollars = round(random.uniform(1, 1000), 2)
    product_id = random.choice(product_ids)
    c.execute("INSERT INTO Orders VALUES (?, ?, ?, ?)", (customer_id, purchase_date, purchase_amt_dollars, product_id))

# Commit changes and close connection
conn.commit()
conn.close()