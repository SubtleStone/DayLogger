#imports

import sqlite3
import pandas as pd



#Database Path
path = r"..\db\data.db"

def finance_handler():
    choice = input(f"\nWhat action do you want to perform?\n{('='*width)}\n1. Log transaction(log)\n2. List transaction(display)\n3. Edit transaction(edit)\n4. Remove transaction(remove)\n")
    match choice:
                case "log":
                    finance_log_input_selection()
                case "display":    
                    finance_display_input_selection()
                case "edit":
                    finance_edit_transaction_handler()
                case "remove":
                    pass    

def finance_log_input_selection():
    print("Logging Selected...")
    log = input("What do you want to log?   (income, expenditure)\n")
    match log:
                        case "income":
                            finance_log_input_selection_income()
                        case "expenditure":
                            finance_log_input_selection_expenditure()

def finance_log_input_selection_income():
    print("loading income entry module...")
    amount = input("Enter the amount\n")
    timestamp = input("Enter the Date and Time\n")
    category = "income"
    tags = input("Enter any relevant tags regarding the income source\n")
    note = input("Any description for the transaction\n")
    transaction_log_add(amount,timestamp,category,tags,note)


def finance_log_input_selection_expenditure():
    amount = input("Enter the amount\n")
    timestamp = input("Enter the Date and Time\n")
    category = "expenditure"
    tags = input("Enter any relevant tags regarding the expenditure(Need or Want)\n")
    note = input("Any description for the transaction\n")
    transaction_log_add(amount,timestamp,category,tags,note)

def finance_display_input_selection():
    print("Finance display module selected...")
    choice = input("What do you wish to see? (balance, transactions)")
    match choice:
        case "balance":
            finance_display_input_selection_balance()
        case "transactions":
            finance_display_input_selection_transactions()

def finance_display_input_selection_balance():
    print("Fetching Balance...")
    get_current_balance()

def finance_display_input_selection_transactions():
    get_transaction_history()

def transaction_log_add(val1, val2, val3, val4, val5):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """
    INSERT INTO transactions (amount, timestamp, category, tags, note) 
    VALUES (?,?,?,?,?);
    """
    cursor.execute(query, (val1, val2, val3, val4, val5))
    conn.commit()
    conn.close()
    print("transaction recorded sucessfully")
    print("returning to main menu....")

def get_current_balance():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = "SELECT amount, category FROM transactions"
    cursor.execute(query)
    all_transactions = cursor.fetchall()
    user_balance = 0

    for transaction in all_transactions:
        amount =  transaction[0]
        category = transaction[1]
        if category.lower() == "income":
            user_balance += amount
        else: 
            user_balance -= amount

    conn.close()
    print("Your balance is ", user_balance)


def get_transaction_history():
    category = input(f"Please enter the transaction type.\n Income\n Expenditure\n{('='*width)}\n")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = f"SELECT transaction_id, amount, timestamp, tags, note  FROM transactions WHERE category = '{category}'"  
    cursor.execute(query)
    all_transactions = cursor.fetchall()

    df = pd.DataFrame(all_transactions, columns = ['id', 'amount', 'timestamp', 'tags', 'note'])
    print(df)
    conn.close()
    

def finance_edit_transaction_handler():
    field = input(f"Which field do you wish to edit")
    while true:
        match field:
            case "amount":
                edit_amount()
            case "date-time":
                edit_timestamp()
            case "category":
                edit_category()
            case "tags":
                edit_tags()
            case "note":
                edit_note()
            case "exit":
                break
            case _ :
                print("pick a valid value")

def edit_timestamp(dt, tid):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """
    UPDATE transactions
    SET timestamp = ?
    WHERE transaction_id = ?
    cursor.execute(query, (dt, tid))
    conn.commit()
    conn.close()
    print("Date-time modified successfully!")
    """

def edit_category(cat,tid):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """
    UPDATE transactions
    SET category = ?
    WHERE transaction_id = ?
    cursor.execute(query, (cat, tid))
    conn.commit()
    conn.close()
    print("Category modified successfully!")
    """
def edit_tags(tg, tid):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """
    UPDATE transactions
    SET tags = ?
    WHERE transaction_id = ?
    cursor.execute(query, (tg, tid))
    conn.commit()
    conn.close()
    print("Tags modified successfully!")
    """
def edit_note(nt, tid):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """
    UPDATE transactions
    SET note = ?
    WHERE transaction_id = ?
    cursor.execute(query, (nt, tid))
    conn.commit()
    conn.close()
    print("Notes modified successfully!")
    """