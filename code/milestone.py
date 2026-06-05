import sqlite3
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