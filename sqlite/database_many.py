import sqlite3

# database in memory temp vanishes after run
# conn = sqlite3.connect(':memory:')

# create a database
conn = sqlite3.connect('many_customer.db')

# create a cursor
c = conn.cursor()

# create a table
# using sql docstring
c.execute("""CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    city TEXT
)""")

# create a list of data each tuple is a row
many_customers = [
    ('Daniel', 'Murphy', 'd_murphy@gmail.com', 'Glasgow'),
    ('crispin','miller','c_miller@gmail.com', 'Edinburgh'),
    ('Holly', 'Hall', 'h_hall@gmail.com', 'Baersden'),
    ('Robin', 'Stewart', 'r_sterwart@gmail.com', 'Loch lammond'),
]

# many_customers = [
#     ('Daniel', 'Crispin', 'Robin', 'Holly'), # tuple first_names
#     ('Murphy','Miller','Stewart','Hall'), # tuple last_names
#     ('d_murphy@gmail.com', 'c_miller@gmail.com', 'r_stewart@gmail.com', 'h_hall@gmail.com'), # tuple emails
#     ('galsgow', 'edinburgh', 'Bearsden', 'loch lamond')  # tuple cities
#     ]

# insert many data into table using tupels
c.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers)

# sucess msg
print("Inserted many rows at once data....")

# commit conn to db
conn.commit()

# close connection
conn.close()
