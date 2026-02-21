import sqlite3

def connect_db():
    conn = sqlite3.connect("inventory.db")
    return conn
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER,
        price REAL
    )
    """)

    conn.commit()
    conn.close()