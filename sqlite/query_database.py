import sqlite3

# connection
conn = sqlite3.connect('many_customer.db')
conn1 = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()
c1 = conn1.cursor()

# Query the databse
# get all whole table
c.execute("SELECT * FROM customers")
c1.execute("SELECT * FROM customers")

# fetch and print on the screen
print("\n----------Many customer DB-----------------")
print("First name, Last name, Email    , City")
# print(*c.fetchall(), sep ='\n')
[print(item) for item in c.fetchall()]
print("-----------Customer DB-----------------")
print("First name, Last name, Email    , City")
# print(*c1.fetchall(), sep ='\n')
[print(item) for item in c1.fetchall()]
print("\n")

# commit conn to db
conn.commit()
conn1.commit()

# close connection
conn.close()
conn1.close()