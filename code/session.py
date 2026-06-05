import sqlite3

def new_session(subject, topic, context, duration, remarks, timestamp):
    conn = sqlite3.connect("..\db\data.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO session(subject, topic, context, duration, remarks, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """