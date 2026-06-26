import sqlite3

def session_handler():
    choice = input("Pick a function (new)")
            match choice:
            case "new":
                pass

def session_handler_new_entry():
        subject = input("enter the subject of the topic")
        topic = input("enter the topic covered")
        context = input("any details regarding this session that you may find useful later on")
        duration = input("enter the duration")
        remarks = input("enter your remarks or thoughts about your experience or performance/ sort of like a self evaluation")
        timestamp = input("enter the timestamp")

        new_session(subject, topic, context, duration. remarks, timestamp)

def new_session(subject, topic, context, duration, remarks, timestamp):
    conn = sqlite3.connect("..\db\data.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO session(subject, topic, context, duration, remarks, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """