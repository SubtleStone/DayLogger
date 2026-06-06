import sqlite3
import pandas as pd
width = 60

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
    


    
