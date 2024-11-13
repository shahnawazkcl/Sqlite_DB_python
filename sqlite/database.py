import sqlite3

# database in memory temp vanishes after run
# conn = sqlite3.connect(':memory:')

# create a database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# create a table
# using sql docstring
# c.execute("""CREATE TABLE customers (
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT,
#     city TEXT
# )""")

# insert data into table
c.execute("INSERT INTO customers VALUES ('Daneil', 'Murphy', 'd_murphy@gmail.com', 'galsgow')")

# sucess msg
print("Inserted data....")

# commit conn to db
conn.commit()

# close connection
conn.close()
