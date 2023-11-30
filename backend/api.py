from flask import Flask

import user, expense

app = Flask(__name__)

@app.route('/create_user/<name, mail, password>', methods=['POST'])
def create_user(name, mail, password):
    return user.create_user(name, mail, password)

@app.route('/delete_user<user_id>', methods=['DELETE']) 
def delete_user(user_id):
    return user.delete_user(user_id)   

@app.route('/add_expense<user_id, amount, category,comments>')
def add_expense(user_id, amount, category,comments):
    return expense.add_expense(user_id, amount, category,comments) 

@app.route('/delete_expense<expense_id>') 
def delete_expense(expense_id):
    return expense.delete_expense(expense_id) 

@app.rout('/edit_expense<expense_id,amount=None,category=None,comments=None>')
def edit_expense(expense_id,amount=None,category=None,comments=None):
    return expense.edit_expense(expense_id,amount,category,comments)

@app.route('/get_expenses<user_id, start_date, end_date, categories>')
def get_expenses(user_id, start_date, end_date, categories=None):
    return expense.get_expenses(user_id, start_date, end_date, categories)

@app.route()