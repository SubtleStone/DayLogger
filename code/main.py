import sqlite3
import finance
import milestone
import session
width = 60 #line width for the separators
print("Welcome Back")
while True:
    choice = input(f"Type the name of the module you want access from the selection below.\n{('=' * width)}\n1. finance\n2. milestone\n3. session\n4. exit\n")
    if choice == "finance":
        choice = input(f"\nWhat action do you want to perform?\n{('='*width)}\n1. Log transaction(log)\n2. List transaction(display)\n3. Edit transaction(edit)\n4. Remove transaction(remove)\n")
        if choice == "log":
            print("Logging Selected...")
            log = input("What do you want to log?   (income, expenditure)\n")
            if log == "income":
                amount = input("Enter the amount\n")
                timestamp = input("Enter the Date and Time\n")
                category = "income"
                tags = input("Enter any relevant tags regarding the income source\n")
                note = input("Any description for the transaction\n")
                finance.transaction_log_add(amount,timestamp,category,tags,note)
            elif log == "expenditure":
                amount = input("Enter the amount\n")
                timestamp = input("Enter the Date and Time\n")
                category = "expenditure"
                tags = input("Enter any relevant tags regarding the expenditure(Need or Want)\n")
                note = input("Any description for the transaction\n")
                finance.transaction_log_add(amount,timestamp,category,tags,note)
        elif choice == "display":    
            print("Finance display module selected...")
            choice = input("What do you wish to see? (balance, transactions)")
            if choice == "balance":
                finance.get_current_balance()
            elif choice == "transactions":
                    finance.get_transaction_history()
        elif choice == "edit":
            pass
        elif choice == "remove":
            pass    
    elif choice == "milestone":
        choice = input("Pick a module (new, view)")
        if choice == "new":
                goal_name = input("enter goal name/title")
                description = input("enter the description for this goal")
                target_hours = input("enter an approximation of the number of hours required to achieve the goal")
                milestone.add_goal(goal_name, description, target_hours)
        if choice == "view":
                milestone.view_goal() 
    elif choice == "session":
        choice = input("Pick a function (new)")
        if choice == "new":
                subject = input("enter the subject of the topic")
                topic = input("enter the topic covered")
                context = input("any details regarding this session that you may find useful later on")
                duration = input("enter the duration")
                remarks = input("enter your remarks or thoughts about your experience or performance/ sort of like a self evaluation")
                timestamp = input("enter the timestamp")

                session.new_session(subject, topic, context, duration. remarks, timestamp)
    elif choice == "exit":
        break