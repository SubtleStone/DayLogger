import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#TABLE CREATION

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    timestamp text,
    category TEXT,
    tags TEXT,
    note TEXT,
    balance_snapshot REAL
    );
    CREATE TABLE IF NOT EXISTS session(
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    topic TEXT,
    context TEXT,
    duration TEXT,
    remarks TEXT,
    timestamp TEXT
    );
    CREATE TABLE IF NOT EXISTS milestone(
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_name TEXT,
    description TEXT,
    target_hours TEXT
    );
""")

# REMOVED  balance_snapshot column

# After giving some thought to it. Realised
# having it would make edits to transaction very painful, balance recalculation  
# and timeline management. So instead the system will instead do realtime read and
# calculation of transaction amount and date for the balance snapshot feature.

cursor.execute("""
ALTER TABLE transactions
DROP COLUMN balance_snapshot;
""")







conn.commit()
conn.close()
print("tables created successfully")