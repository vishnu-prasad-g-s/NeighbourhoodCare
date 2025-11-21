import sqlite3

def init_db():
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()

    # Requests table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        address TEXT,
        task TEXT,
        urgency TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)

    # Volunteers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS volunteers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        skills TEXT,
        radius INTEGER,
        availability TEXT
    )
    """)

    conn.commit()
    conn.close()

