'''
User Account Management Script

This script provides basic functionality for managing user accounts in a system.
It allows for creating, deleting, and retrieving user information and interacts
with a CSV file to store and manage this data.

Modules and Global Variables:
    - uuid: Used to generate unique identifiers for new user accounts.
    - csv: Handles reading from and writing to CSV files.
    - USERS_FILE: Path to the CSV file where user data is stored.
'''
import uuid
import csv

USERS_FILE = '../dataBase/users.csv'
# TODO: Need to hash the password in this module, and error heandling in every function, need doucomentation on the functions 
def create_user(name, mail, password):
    '''
    - Purpose: Creates a new user account with the given name, email, and password.
        - Parameters:
            - name: The name of the user.
            - mail: The email address of the user.
            - password: The password for the user account.
        - Returns: The newly created user's information as returned by `get_user`.
        - Details: Generates a unique user ID using `uuid` and writes the user's information to the `USERS_FILE`.
    '''

    user_id = uuid.uuid4().hex
    
    account = {'user_id': user_id,
              'name': name,
              'mail': mail,
              'password': password}
    
    with open(USERS_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=account.keys())
        writer.writerow(account)

    return get_user(name, password)


def delete_user(user_id):
    '''
        delete_user(user_id):
        - Purpose: Deletes a user account from the system based on their user ID.
        - Parameters:
            - user_id: The unique identifier of the user to be deleted.
        - Returns: The information of the removed user.
        - Details: Reads all users from `USERS_FILE`, filters out the user with the specified `user_id`, and writes the updated list back to the file. Note: The function contains a TODO item regarding the handling of associated user data (like expenses and categories).
    '''

    users = []
    removed_user = None
    fields = None
    
    with open(USERS_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        for row  in reader:
            if row[0] != user_id:
                users.append(row)
            else:
                removed_user = row

    with open(USERS_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(users)
    # TODO: need to remove all user expenses and categories data where and when to do it?
    return removed_user         # Do I need to return it as a json dict   

def get_user(name, password):
    '''
       get_user(name, password):
        - Purpose: Retrieves a user's information based on their name and password.
        - Parameters:
            - name: The name of the user.
            - password: The password of the user account.
        - Returns: The user's information if found, otherwise `None`.
        - Details: Searches for a user in `USERS_FILE` whose name and password match the provided values.
    '''

    user = None
    
    with open(USERS_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None) 
        for row  in reader:
            if row[1] == name and row[3] == password:
                user = row
                break

    return user     # Do I need to return it as a json dict   



def main():
    pass
if __name__ == '__main__':
    main()

'''
Notes and TODOs:
    - The script includes TODO comments about hashing passwords and error handling, which are important for security and robustness.
    - The `delete_user` function needs to handle the removal of associated user data, which is not currently implemented.
    - The return format (e.g., JSON dictionary) for some functions is under consideration.

Security and Improvements:
    - Passwords are currently stored in plain text, which is a significant security risk. Implementing password hashing is crucial.
    - Error handling is not implemented, which should be addressed for production use.
    - The script does not validate input data, leaving it prone to errors or malicious inputs.
'''