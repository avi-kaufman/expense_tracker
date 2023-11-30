'''
Expense Management Script

This script is designed to manage financial expenses for users. It provides functionalities
to add, delete, edit, and retrieve expense data. The script interacts with a CSV file to
store and manage this data.

Modules and Global Variables:
    - uuid: Used for generating unique identifiers for each expense entry.
    - csv: Used for reading from and writing to CSV files.
    - datetime: Used to handle dates and times for each expense entry.
    - EXPENSES_FILE: Path to the CSV file where expense data is stored.
'''
import uuid
import csv
from datetime import datetime

EXPENSES_FILE = '../dataBase/expenses.csv'

def add_expense(user_id, amount, category,comments):
    '''
    - Purpose: Adds a new expense entry for a user.
        - Parameters:
            - user_id: Identifier for the user who made the expense.
            - amount: The monetary value of the expense.
            - category: The category to which the expense belongs.
            - comments: Any additional comments regarding the expense.
        - Returns: Details of the newly added expense entry.
        - Details: Generates a unique expense ID and records the current date and time for both creation and last update.
    
    '''

    expense_id = uuid.uuid4().hex
    created_at, updated_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    expense = {'expense_id': expense_id,
               'user_id': user_id,
               'amount': amount,
               'category': category,
               'comments': comments,
               'created_at': created_at,
               'updated_at': updated_at} # do I need to insert updated_at

    with open(EXPENSES_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=expense.keys())
        writer.writerow(expense)

    return get_expense(expense_id)    

def delete_expense(expense_id):
    '''
    - Purpose: Deletes an expense entry based on its ID.
        - Parameters:
            - expense_id: The unique identifier of the expense to be deleted.
        - Returns: The details of the removed expense entry.
        - Details: Reads all expenses from EXPENSES_FILE, filters out the expense with the specified expense_id, and rewrites the updated list back to the file. 
    '''

    expenses = []
    removed_expense = None
    fields = None

    with open(EXPENSES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        for row in reader:
            if row[0] != expense_id:
                expenses.append(row)
            else:
                removed_expense = row

    with open(EXPENSES_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(expenses)

    return removed_expense                

def edit_expense(expense_id,amount=None,category=None,comments=None):
    '''
    Purpose: Edits an existing expense entry.
        - Parameters:
            - expense_id: The unique identifier of the expense to be edited.
            - amount: (Optional) New amount for the expense.
            - category: (Optional) New category for the expense.
            - comments: (Optional) New comments for the expense.
        - Returns: The details of the edited expense entry.
        - Details: Updates the specified fields of the expense and the updated_at timestamp.
    
    '''
    expenses = []
    edited_expense = None
    fields = None

    with open(EXPENSES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        for row in reader:
            if row[0] != expense_id:
                expenses.append(row)
            else:
                edited_expense = row
                
    if amount:
        edited_expense[2] = amount
    if category:
        edited_expense[3] = category
    if comments:
        edited_expense[4] = comments
    
    edited_expense[6] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    expenses.append(edited_expense) 

    with open(EXPENSES_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(expenses)

    return edited_expense 

#need to add user_id when searching
def get_expenses(user_id, start_date, end_date, categories=None): # Get expense by age and by categories
    '''
    - Purpose: Retrieves expenses for a user based on age and optional categories.
        - Parameters:
            - user_id: The user's identifier.
            - age: The age filter for the expenses.
            - categories: (Optional) Specific categories to filter the expenses.
        - Returns: A list of expenses matching the criteria.
        - Details: Filters expenses from EXPENSES_FILE based on the provided parameters.
    '''

    expenses = []
    with open(EXPENSES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        if categories:
            for row in reader:
                if row[3] in categories and row[4]< age:# how to implement this logic
                    expenses.append(row)

        else: # how to implement the logic of the if else in elegant way
            for row in reader:
                if  row[4]< age:# how to implement this logic
                    expenses.append(row)
        
    return expenses

def get_expense(expense_id): # get expenses by expense id
    '''
    - Purpose: Retrieves details of a specific expense entry.
        - Parameters:
            - expense_id: The unique identifier of the expense.
        - Returns: The details of the specified expense entry.
        - Details: Searches EXPENSES_FILE for an expense matching the given expense_id.
    '''
    expense = None
    with open(EXPENSES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            if row[0] == expense_id:
                expense = row
                break

    return expense

def main():
    pass

if __name__ == '__main__':
    main()

'''
Notes and Improvements:
    - The script contains several TODO comments and questions about implementation.
    - The logic for filtering expenses by age in get_expenses needs to be properly implemented.
    - Security and validation aspects are not addressed, which are important for handling financial data.
'''