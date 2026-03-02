import sqlite3

# Create database and users table
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Add some test users
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user', 'password'))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('test', 'test123'))

conn.commit()
conn.close()

print("Database created successfully!")
print("Test users:")
print("  - admin / admin123")
print("  - user / password")
print("  - test / test123")
