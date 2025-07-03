import sqlite3

def setup_db():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Links(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Link TEXT)")
    conn.commit()
    conn.close()
    print("Database setup complete")
