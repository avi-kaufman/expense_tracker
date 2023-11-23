import csv

EXPENSES_FILE = '../dataBase/expense.csv'

def spent_on_category(user_id, start_date, end_date, category_name):
    spent = 0
    with open(EXPENSES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)     
        next(reader) # reed the filds
        for row in reader:
            if row[1] == user_id and row[5] >= start_date and row[5]<=end_date and row[3] == category_name:# need to implement the age condition
                spent += float(row[2])

    return spent            

def mean(user_id, age, category_id):
    pass

def main():
    pass

if __name__ == '__main__':
    main()