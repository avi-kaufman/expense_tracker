import uuid
import csv
from datetime import datetime

EXPENSES_FILE = '../dataBase/expenses.csv'

def add_expense(user_id, amount, category,comments):
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
                break

    with open(EXPENSES_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(expenses)

    return removed_expense                

def edit_expense(expense_id,amount=None,category=None,comments=None):
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
                break
    
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

def get_expenses(age, categories=None): # Get expense by age and by categories
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