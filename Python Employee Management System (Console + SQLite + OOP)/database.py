import sqlite3

def connect_db():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary REAL
    )
    """)

    conn.commit()
    return conn, cursor