import sqlite3

conn = sqlite3.connect('many_customer.db')

c = conn.cursor()

# 01 : use WHERE clause
# c.execute("select * from customers where first_name like 'D%'")

# 02: update records and the print 
# c.execute("""UPDATE customers SET first_name = 'Crispin'
#         WHERE last_name = 'miller'
#         """)

# 03: update records using rowid and the print 
# c.execute("""UPDATE customers SET last_name = 'Miller'
#         WHERE rowid = 2
#         """)

# 04: Delete records using rowid and the print 
# c.execute("DELETE from customers WHERE rowid = 3")

# conn.commit()

# use WHERE clause
# c.execute("SELECT rowid, * FROM customers")

# 05: use ORDER BY using column ASC/DESC
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")

# 06: use AND/OR to bind two condition
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'M%' AND first_name LIKE 'C%'")

# 07: use LIMIT for getting certain umber of results from large tabels
# c.execute("SELECT rowid, * FROM customers LIMIT 2")

# 08: deletin /drop the table
# :wraning: use this only when u are sure.
c.execute("DROP TABLE customers")

# using list comprehension to print the query output
[print(item) for item in c.fetchall()]

conn.commit()
conn.close()
