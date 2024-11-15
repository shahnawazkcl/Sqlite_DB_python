import sqlite3

# create connection function
def connect_to_database(db_name):
    """creates a connection to the named database

    Args:
        db_name (string): name of the database

    Returns:
        connection: connection to the database
    """
    connection = sqlite3.connect(db_name)
    return connection

# query the database and return all records
def show_all(table_name):
    """fetch all the records in the table

    Args:
        table_name (string): name of the table to fetch records from.
    """
    conn = connect_to_database('thisApp.db')
    # use error handling
    try:
        c = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        c.execute(query)
        print(f"Records in '{table_name}' table:")
        [print(item) for item in c.fetchall()]
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
    finally:
        if conn:
            conn.close()
            print('SQLite Connection closed')

# add a new record to the table.
def add_records(records: list, table_name: str):
    """
    Add new record(s) in the given table.

    Args:
        records (list): List of the records as tuples.
        table_name (str): Name of the table.
    """
    conn = connect_to_database('thisApp.db')
    try:
        c = conn.cursor()

        # Dynamically generate placeholders based on the number of fields in each record
        num_placeholders = len(records[0]) if records else 0
        placeholders = ', '.join(['?'] * num_placeholders)

        # Parameterized query to prevent SQL injection
        ins_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

        # Use executemany to handle multiple records
        c.executemany(ins_query, records)
        print(f"Inserting {len(records)} records into '{table_name}' table:")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting records: {e}")
    finally:
        if conn:
            conn.close()
            print('Connection to DB closed after inserting.')


# delete records from the given table
def delete_records(record:list, table_name):
    """Delete record(s) in the given table

    Args:
        record (list): list of the records as tuples
        table_name (string): name of the table

    """
    conn = connect_to_database('thisApp.db')
    try:
        c = conn.cursor()
        print(f"Deleting {len(record)} records from '{table_name}' table:")
        # Use placeholders for the query to prevent SQL injection
        placeholders = ', '.join(['?'] * len(record))
        del_query = f"DELETE FROM {table_name} WHERE rowid IN ({placeholders})"
        c.execute(del_query, tuple(record))
        conn.commit()  # Commit the changes
    except sqlite3.Error as e:
        print(f"Error deleting records: {e}")
    finally:
        if conn:
            conn.close()
            print('Connection to DB closed after deleting')

# add lookup function using where clause.
def lookup_record(search_str: str, table_name: str, colname: str):
    """
    Search a table for any value in a specific column.

    Args:
        search_str (str): Search string.
        table_name (str): Name of the table.
        colname (str): Name of the column to search.

    Returns:
        List of matching rows.
    """
    conn = connect_to_database('thisApp.db')
    try:
        c = conn.cursor()
        # Use a parameterized query to prevent SQL injection
        query = f"SELECT * FROM {table_name} WHERE {colname} LIKE ?"
        c.execute(query, (f"%{search_str}%",))  # Add wildcards for partial matching
        results = c.fetchall()

        if results:
            print(f"Found {len(results)} record(s) matching '{search_str}' in column '{colname}':")
            for row in results:
                print(row)
        else:
            print(f"No records found matching '{search_str}' in column '{colname}'.")

        return results
    except sqlite3.Error as e:
        print(f"Error during lookup: {e}")
        return []
    finally:
        if conn:
            conn.close()
            print('Connection to DB closed after lookup.')
