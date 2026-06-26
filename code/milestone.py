import sqlite3

def milestone_handler():
    action = input("Pick a module (new, view)")
            match action:
            case "new":
                    milestone_new_record_entry()
            case "view":
                    milestone_view_records()                

def  milestone_new_record_entry():
    goal_name = input("enter goal name/title")
                    description = input("enter the description for this goal")
                    target_hours = input("enter an approximation of the number of hours required to achieve the goal")
                    add_goal(goal_name, description, target_hours)

def milestone_view_records():
    view_goal()

def add_goal(val1, val2, val3):
    conn = sqlite3.connect("..\db\data.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO milestone(goal_name, description, target_hours)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (val1, val2, val3))
    conn.commit()
    conn.close()
    print("Milestone added sucessfully!!!")
    print("Returning to main menu....")

def view_goal():
    conn = sqlite3.connect("..\db\data.db")
    cursor = conn.cursor()
    query = """
    SELECT milestone_id, goal_name, description, target_hours FROM milestone
    """
    cursor.execute(query)
    all_goals = cursor.fetchall()
    
    print("\tId", "\tName", "\tDescription", "\tHours")
    for goal in all_goals:
        id = goal[0] 
        name = goal[1]
        description = goal[2]
        hours = goal[3]
        print("\t", id, "\t", name, "\t", description, "\t", hours)
    
    conn.close()
    print("records fetched succesfully!!!")
    print("Returning to main menu....")