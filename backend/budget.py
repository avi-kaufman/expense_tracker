'''
Budget Management Script

This script provides functionalities for managing budget data for users. It includes
functions to add, delete, edit, and retrieve budget data, interacting with a CSV file
to store and manage this data.

Modules and Global Variables:
    - uuid: Used for generating unique identifiers for budget categories.
    - csv: Used for reading from and writing to CSV files.
    - CATEGORIES_FILE: Path to the CSV file where category data is stored.
    - BUDGET_FILE: Path to the CSV file where budget data is stored.
'''

import csv
import uuid

CATEGORIES_FILE = '../dataBase/categories.csv'
BUDGET_FILE = '../dataBase/budget.csv'

def add_budget(user_id, category_name, monthly_budget):
    '''
    - Purpose: Adds a new budget entry for a user.
    - Parameters:
        - user_id: Identifier for the user.
        - category_name: Name of the category for the budget.
        - monthly_budget: The amount allocated for the budget.
    - Returns: The newly created budget entry.
    - Details: Generates a unique category ID (if new) and writes the budget information to the BUDGET_FILE.
    '''
    category_id = get_category_id(category_name)
    
    budget = {'user_id': user_id,
              'category_id': category_id,
              'monthly_budget': monthly_budget}
    
    with open(BUDGET_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=budget.keys())
        writer.writerow(budget)

    return get_budget(user_id, category_id)    

def delete_budget(user_id, category_id):
    '''
    - Purpose: Deletes a budget entry based on user ID and category ID.
        - Parameters:
            - user_id: The user's identifier.
            - category_id: The identifier of the budget category to be deleted.
        - Returns: The details of the removed budget entry.
        - Details: Reads all budgets from BUDGET_FILE, filters out the specified budget entry, and rewrites the updated list back to the file.

    '''
    budgets = []
    removed_budget = None
    fields = None

    with open(BUDGET_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        for row in reader:
            if row[0] != user_id or row[1] != category_id:
                budgets.append(row)
            else:
                removed_budget = row
                
    print(budgets)
    with open(BUDGET_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)          
        writer.writerows(budgets)

    return removed_budget

def edit_budget(user_id,category_id, category_name=None, monthly_budget=None):
    '''
    - Purpose: Edits an existing budget entry.
        - Parameters:
            - user_id: The user's identifier.
            - category_id: The identifier of the budget category to be edited.
            - category_name: (Optional) New name for the budget category.
            - monthly_budget: (Optional) New amount for the budget.
        - Returns: The details of the edited budget entry.
        - Details: Updates the specified fields of the budget entry.
    '''
    budget = []
    edited_budget = []
    fields = None

    with open(BUDGET_FILE, 'r') as csvfiele:
        reader = csv.reader(csvfiele)
        fields = next(reader)
        for row in reader:
            if row[0] != user_id or row[1] != category_id:
                budget.append(row)
            else:
                edited_budget = row.copy()
                if category_name:
                    edited_budget[1] = get_category_id(category_name)
                if monthly_budget:
                    edited_budget[2] = monthly_budget 

    budget.append(edited_budget)

    with open(BUDGET_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(budget)   

    return get_budget(user_id, edited_budget[1])                


def get_category_id(category_name): # Get category id by name if not in the csv write it and return the id
    '''
    - Purpose: Retrieves or creates a unique identifier for a budget category.
       - Parameters:
           - category_name: The name of the budget category.
       - Returns: The unique identifier for the specified category.
       - Details: Searches for the category in CATEGORIES_FILE and creates a new entry if it does not exist.
    '''
    category_id = None
    with open(CATEGORIES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == str(category_name):
                category_id = row[0]
                break
        if category_id == None:
            category_id = uuid.uuid4().hex
        
            category = {'category_id': category_id,
                        'category_name': category_name}
            
            with open(CATEGORIES_FILE, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=category.keys())
                writer.writerow(category)

    return category_id

def get_budgets(user_id): # Get all user categories
    '''
    - Purpose: Retrieves all budget entries for a specific user.
        - Parameters:
            - user_id: The user's identifier.
        - Returns: A list of all budget entries for the user.
        - Details: Filters budget entries from BUDGET_FILE based on the user_id.
    '''

    budgets = []

    with open(BUDGET_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            if row[0] == user_id:
                budgets.append(row)

    return budgets        

def get_budget(user_id, category_id):
    '''
    - Purpose: Retrieves a specific budget entry.
        - Parameters:
            - user_id: The user's identifier.
            - category_id: The identifier of the budget category.
        - Returns: The details of the specified budget entry.
        - Details: Searches BUDGET_FILE for a budget entry matching the given user_id and category_id.
    '''
    with open(BUDGET_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == user_id and row[1] == category_id:
                return row
    
    return None
        
def main():
    pass
    
if __name__ == '__main__':
    main()