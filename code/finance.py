#imports

import sqlite3
import pandas as pd
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Button, Label, Input, DataTable


#Database Path
path = r"..\db\data.db"


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

def get_current_balance() -> float:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    query = """
    SELECT
        COALESCE(SUM(CASE WHEN LOWER(category) = 'income' THEN amount ELSE 0 END), 0) - 
        COALESCE(SUM(CASE WHEN LOWER(category) = 'expenditure' THEN amount ELSE 0 END), 0)
    AS current_balance FROM transactions;
    """
    
    cursor.execute(query)
    # all_transactions = cursor.fetchall()
    # user_balance = 0

    # for transaction in all_transactions:
    #     amount =  transaction[0]
    #     category = transaction[1]
    #     if category.lower() == "income":
    #         user_balance += amount
    #     else: 
    #         user_balance -= amount
    user_balance = cursor.fetchone()
    conn.close()

    return float(user_balance[0] if user_balance else 0.0)


def get_transaction_history():
    #category = input(f"Please enter the transaction type.\n Income\n Expenditure\n{('='*width)}\n")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    query = """SELECT transaction_id, category, amount, tags, note, timestamp  
    FROM transactions
    ORDER BY timestamp DESC
    LIMIT 100;
    """  
    cursor.execute(query)
    all_transactions = cursor.fetchall()

    #df = pd.DataFrame(all_transactions, columns = ['id', 'amount', 'timestamp', 'tags', 'note'])
    return all_transactions
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





class FinanceMenu(Screen):
    """Sub menu screen for handling finance  match cases"""
    CSS = """
    #navbar {
        layout: horizontal;
        height: 3;
        background: #2c3e50;
        margin-bottom: 1;
    }
    #navbar Button{
        width: auto;
        height: 100%;
        margin-right: 2;
        border: none;

    }

    #main_content{
        padding:  1 2;
        background: #1e1e1e;
    }

    #lbl_balance {
       # font-size: 1;
        margin-bottom: 2;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="navbar"):
           #yield Label("Financial Management Sub-Menu")
            yield Button("Log Transaction", id="fin_log")
            # yield Button("List Transaction", id="fin_display")
            # yield Button("Edit Transaction", id="fin_edit")
            # yield Button("Remove Transaction", id="fin_remove", variant="warning")
            yield Button("Go Back", id = "fin_back")

        with Vertical(id="main_content"):
                yield Label("Current balance", id="lbl_balance")
                yield DataTable(id="history_table", cursor_type = "row")


        yield Footer()
     
    def on_mount(self)->None:
        try: 
            balance = get_current_balance()
            if balance > 0:
                status_text = f"Your balance is : {balance}"
            else:
                status_text = f"Your balance is : {balance}"
            self.query_one("#lbl_balance", Label).update(status_text)

        except Exception as e:
            self.query_one("#lbl_balance", Label).update(f"[red]Encounter error : {e}[/red]")

        table = self.query_one("#history_table", DataTable)
        #transaction_id, category, amount, tags, note, timestamp
        table.add_columns("ID", "Type", "Amount", "Tags", "Notes","Date/Time") 

        try:
            db_rows = get_transaction_history()

            for row in db_rows:
                tx_id, type, amount, tag, note, datetime = row

                if type.lower() == "income":
                    colored_amount = f"[green]+${amount:,.2f}[/green]"
                else:
                    colored_amount = f"[red]-${amount:,.2f}[/red]"

                table.add_row(
                    str(tx_id),
                    str(type),
                    colored_amount,
                    str(tag),
                    str(note),
                    str(datetime)
        )

        except Exception as e:
            self.notify(f"Error: failed  to load the table :{e}", severity = "error")




    def on_button_pressed(self, event: Button.Pressed) -> None:

        button_id = event.button.id or ""
        button_id = button_id.strip()

        if not event.button.id:
            return
        
        match button_id:
            case "fin_log":
                self.notify("Logging Module activated")
                self.app.push_screen(FinanceLog())
            case "fin_display":
                self.notify("Apologies Display Module is yet to be implemented!")
            case "fin_edit":
                self.notify("Apologies Edit module will be implemented soon")
            case "fin_back":
                self.dismiss()
                event.stop() #this stops the false unknown button action trigger below from firing
            case "fin_remove":
                self.notify("Apologies Remove module hasn't been implemented yet")
            case "":
                pass
            case _:
                self.notify("unknown button action please select again")

   

    # def finance_handler():
    #     choice = input(f"\nWhat action do you want to perform?\n\n1. Log transaction(log)\n2. List transaction(display)\n3. Edit transaction(edit)\n4. Remove transaction(remove)\n")
    #     match choice:
    #                 case "log":
    #                     finance_log_input_selection()
    #                 case "display":    
    #                     finance_display_input_selection()
    #                 case "edit":
    #                     finance_edit_transaction_handler()
    #                 case "remove":
    #                     pass    

class FinanceLog(Screen):
        def compose(self) -> ComposeResult:
            yield Header()
            yield Label("Is the transaction an income or an expense?")
            yield Button("Income", id="btn_income")
            yield Button("Expense", id="btn_expense")
            yield Button("Go Back", id="btn_previous")

            yield Footer()

        def on_button_pressed(self, event: Button.Pressed) -> None:

            button_id = event.button.id or ""
            button_id = button_id.strip()

            match button_id:
                case "btn_income":
                    self.app.push_screen(IncomeInputScreen())
                case "btn_expense":
                    self.app.push_screen(ExpenseInputScreen())
                case "btn_previous":
                    self.dismiss()
                    event.stop()
                    pass
                case _:
                    self.notify("Invalid button event")
                

            
class IncomeInputScreen(Screen):
    def compose(self)->ComposeResult:
        yield Header()
        yield Label("---INCOME LOG---")

        yield Label("Amount")
        yield Input(placeholder="eg. = 1500.00", id = "inp_amount")

        yield Label("Date and Time")
        yield Input(placeholder="YYYY-MM-DD HH:MM", id="inp_timestamp")

        yield Label("Tags")
        yield Input(placeholder="eg. = salary, freelance, gift", id="inp_tags")

        yield Label("Description / Note:")
        yield Input(placeholder="where/whom did this  money come from", id="inp_note")

        yield Button("Submit Transaction", id="btn_submit", variant="success")
        yield Button("Cancel", id="btn_cancel", variant="error")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed)->None:
        button_id=(event.button.id or "").strip()

        match button_id:
            case "btn_submit":
                amount_val = self.query_one("#inp_amount", Input).value
                timestamp_val = self.query_one("#inp_timestamp", Input).value
                tags_val = self.query_one("#inp_tags", Input).value
                note_val = self.query_one(
                    "#inp_note", Input
                ).value
                
                category_val = "income"
                
                if not amount_val:
                    self.notify("Amount cannot be empty!", variant = "error")
                    return
                
                try:
                    transaction_log_add(amount_val, timestamp_val, category_val, tags_val, note_val)
                    self.notify("Income logged successfully!")

                    self.dismiss()
                    event.stop()
                except Exception as e:
                    self.notify(f"Database Error: {str(e)}", severity="error")

            case "btn_cancel":
                self.dismiss()
                event.stop()

            case _:
                self.notify("Invalid option.")


class ExpenseInputScreen(Screen):
    def compose(self)->ComposeResult:
        yield Header()
        yield Label("Expense Log")
        yield Label("Amount:")
        yield Input(placeholder = "e.g. 1523.00", id="inp_amount")
        yield Label("Date and Time:")
        yield Input(placeholder = "YYYY-MM-DD HH:MM", id="inp_timestamp")
        yield Label("Tags")
        yield Input(placeholder = "eg. emi, loan payment, electricity bill, etc", id = "inp_tags")
        yield Label("Description / Note :")
        yield Input(placeholder = "Where/Whom did the money go to and brief description", id = "inp_note")

        yield Button("Submit Transaction", id="btn_submit", variant = "success")
        yield Button("Cancel", id = "btn_cancel", variant = "error")
        yield Footer()

    def on_button_pressed(self, event : Button.Pressed) -> None:
        button_id = (event.button.id or "").strip()
        match button_id:
            case "btn_submit":
                amount_val = self.query_one("#inp_amount", Input).value
                timestamp_val = self.query_one("#inp_timestamp", Input).value
                tags_val = self.query_one("#inp_tags", Input).value
                note_val = self.query_one("#inp_note", Input).value
                category_val = "expense"

                if not amount_val: 
                    self.notify("amount cannot be empty!", variant = "error")
                    return

                try: 
                    transaction_log_add(amount_val, timestamp_val, category_val, tags_val, note_val)
                    self.notify("Expense Logged Successfully")

                    self.dismiss()
                    event.stop()
                except Exception as e:
                    self.notify("Database error {str(e)}", severity = "error")

            case "btn_cancel":
                self.dismiss()
                event.stop()

            case _:
                self.notify("Invalid Option")


    # def finance_log_input_selection():
    #     print("Logging Selected...")
    #     log = input("What do you want to log?   (income, expenditure)\n")
    #     match log:
    #                         case "income":
    #                             finance_log_input_selection_income()
    #                         case "expenditure":
    #                             finance_log_input_selection_expenditure()

    # def finance_log_input_selection_income():
    #     print("loading income entry module...")
    #     amount = input("Enter the amount\n")
    #     timestamp = input("Enter the Date and Time\n")
    #     category = "income"
    #     tags = input("Enter any relevant tags regarding the income source\n")
    #     note = input("Any description for the transaction\n")
    #     transaction_log_add(amount,timestamp,category,tags,note)


    # def finance_log_input_selection_expenditure():
    #     amount = input("Enter the amount\n")
    #     timestamp = input("Enter the Date and Time\n")
    #     category = "expenditure"
    #     tags = input("Enter any relevant tags regarding the expenditure(Need or Want)\n")
    #     note = input("Any description for the transaction\n")
    #     transaction_log_add(amount,timestamp,category,tags,note)

    # def finance_display_input_selection():
    #     print("Finance display module selected...")
    #     choice = input("What do you wish to see? (balance, transactions)")
    #     match choice:
    #         case "balance":
    #             finance_display_input_selection_balance()
    #         case "transactions":
    #             finance_display_input_selection_transactions()

    