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
c.execute("""UPDATE customers SET last_name = 'Miller'
        WHERE rowid = 2
        """)

conn.commit()

# use WHERE clause
c.execute("SELECT rowid, * FROM customers")

# using list comprehension to print the query output
[print(item) for item in c.fetchall()]

conn.close()
