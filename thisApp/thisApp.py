import thisApp_db

# todo : Add funtions to get user input for inserting 
# and deleting records and serching

if __name__ == "__main__":
    table_name = "users"
    # records_to_insert = [
    #     (10, 'Alice', 25, 'alice@gmail.com'),
    # ]
    # records_to_delete = [10]
    
    # thisApp_db.add_records(records_to_insert, table_name)
    
    # print("\n=== Records before Deleting ===")
    # thisApp_db.show_all(table_name)
    
    # print("\n=== Delete Records ===")
    # thisApp_db.delete_records(records_to_delete, table_name)
    
    # print("\n=== Records after deleting ===")
    # thisApp_db.show_all(table_name)
    
    # Search for a user by name
    search_term = input("Enter a name to search for: ")
    # matching_records = thisApp_db.lookup(search_term, table_name, 'name')

    # if matching_records:
    #     print("\nMatching Records:")
    #     for record in matching_records:
    #         print(record)
    thisApp_db.lookup_record(search_term, table_name, 'name')
