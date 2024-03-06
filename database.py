import os

def load_database(filename):
    names_db = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, count = line.strip().split(',')
                names_db[name] = int(count)
    return names_db

def save_database(names_db, filename):
    with open(filename, 'w') as file:
        for name, count in names_db.items():
            file.write(f"{name},{count}\n")

def search_name(names_db, name):
    """ Searches a given name on the database and returns its count or None if not found
    """
    return names_db.get(name)

def add_name(names_db, name):
    """ Add name  to the database and increase its counter by 1

    Args:
      names_db (dict): A dictionary containing the database of names and their counts.
      name (str): The name to be added to the database.
    """
    names_db[name] = names_db.get(name, 0) + 1

def delete_name(names_db, name):
    """ Delete names from name_db

    Args:
      names_db (dict): A dictionary containing the database of names and their counts.
      name (str): The name to be deleted from the database.
    
    Returns:
    name (str): if name exist
    str: if name not found
    """
    if name in names_db:
      return names_db.pop(name)
    else: 
      return f"{name} not found."

def edit_name(names_db, newName, oldname):
    """ Edit names from name_db

    Args: 
    names_db (dict): A dictionary containing the database of names and their counts.
    newName(str): the new name set buy user
    oldname(str): The current name that will be changed to new one by user
    
    Returns:
    dict : updated names_db after changing a name
    """
    if oldname in names_db:
      count = names_db.pop(oldname)
      names_db[newName] = count
      return names_db


def main():
    db_filename = "names_database.txt"
    names_db = load_database(db_filename)
    
    while True:
        print("1. Search name")
        print("2. Add name")
        print("3. Edit name")
        print("4. View all names")
        print("5. Delete name")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name to search: ")
            count = search_name(names_db, name)
            if count is not None:
                print(f"{name} found! Count: {count}")
            else:
                print(f"{name} not found in the database.")
        elif choice == "2":
            name = input("Enter name to add: ")
            add_name(names_db, name)
            print(f"{name} added to the database.")
        elif choice == '3':
            for i in names_db:
              print(i)
            oldName = input("Choose name to edit: ")
            newName = input("Enter new name: ")
            edit_name(names_db, newName, oldName)
            print(f"{oldName} has been change to {newName} in the database.")
        elif choice == '4':
            print("Names: ")
            for i in names_db:
                print(i)
        elif choice == '5':
            for i in names_db:
                print(i)
            n = input("Choose name to delete: ")
            delete_name(names_db, n)
            print(f"{n} has been deleted in the database.")
        elif choice == "6":
            save_database(names_db, db_filename)
            print("Database saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
