import sqlite3

# Function to connect to the SQLite database (or create it if it doesn't exist)
def connect_to_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

# Function to create a table
def create_table(connection, table_name, columns):
    """
    Creates a table in the database.
    :param connection: Database connection object
    :param table_name: Name of the table
    :param columns: Dictionary of columns with column name as key and column type as value
    """
    try:
        cursor = connection.cursor()
        column_defs = ', '.join([f"{col} {col_type}" for col, col_type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
        cursor.execute(query)
        connection.commit()
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Function to insert data into a table
def insert_data(connection, table_name, data):
    """
    Inserts a record into the table.
    :param connection: Database connection object
    :param table_name: Name of the table
    :param data: Dictionary where keys are column names and values are the corresponding data
    """
    try:
        cursor = connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(data.values()))
        connection.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# Function to fetch and display all records from a table
def fetch_all_records(connection, table_name):
    """
    Fetches all records from the table and displays them.
    :param connection: Database connection object
    :param table_name: Name of the table
    """
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"Records in '{table_name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

# Main script logic
if __name__ == "__main__":
    db_name = "thisApp.db"
    table_name = "users"
    columns = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "age": "INTEGER",
        "email": "TEXT"
    }

    # Data to insert
    user_data = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": 30, "email": "bob@example.com"},
        {"name": "Charlie", "age": 35, "email": "charlie@example.com"},
        {"name": 'Daniel', "age": 45, "email": 'd_murphy@gmail.com'},
        {"name": 'crispin',"age": 55,"email": 'c_miller@gmail.com'},
        {"name": 'Holly', "age": 30, "email": 'h_hall@gmail.com'},
        {"name": 'Robin', "age": 50, "email": 'r_sterwart@gmail.com'},
    ]

    # Connect to the database
    connection = connect_to_database(db_name)

    # Create the table
    create_table(connection, table_name, columns)

    # Insert data
    for data in user_data:
        insert_data(connection, table_name, data)

    # Fetch and display all records
    fetch_all_records(connection, table_name)

    # Close the connection
    connection.close()
