import sqlite3
import pandas as pd
width = 60

def finance_handler():
    action = input(f"\nWhat action do you want to perform?\n{('='*width)}\n1. Log transaction(log)\n2. List transaction(display)\n3. Edit transaction(edit)\n4. Remove transaction(remove)\n")
            match action:
                case "log":
                    finance_log_input_selection():
                case "display":    
                    finance_display_input_selection()
                case "edit":
                    pass
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
                            finance_display_input_selection_transactions

def finance_display_input_selection_balance():
    print("Fetching Balance...")
    get_current_balance()

def finance_display_input_selection_transactions():
    get_transaction_history()

def transaction_log_add(val1, val2, val3, val4, val5):
    conn = sqlite3.connect("..\db\data.db")
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
    conn = sqlite3.connect("..\db\data.db")
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
    conn = sqlite3.connect("..\db\data.db")
    cursor = conn.cursor()
    query = f"SELECT transaction_id, amount, timestamp, tags, note  FROM transactions WHERE category = '{category}'"  
    cursor.execute(query)
    all_transactions = cursor.fetchall()

    df = pd.DataFrame(all_transactions, columns = ['id', 'amount', 'timestamp', 'tags', 'note'])
    print(df)
    conn.close()
    


    
