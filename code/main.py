import sqlite3
import finance
import milestone
import session
width = 60 #line width for the separators
print("Welcome Back")
while True:
    choice = input(f"Type the name of the module you want access from the selection below.\n{('=' * width)}\n1. finance\n2. milestone\n3. session\n4. exit\n")
    
    match choice:
        case "finance":
            finance.finance_handler()
        case "milestone":
            milestone.milestone_handler()
        case "session":
            session.session_handler()s
        case == "exit":
            break