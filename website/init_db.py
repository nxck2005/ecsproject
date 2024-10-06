import sqlite3

# Connect to database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reg_num TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully!")
