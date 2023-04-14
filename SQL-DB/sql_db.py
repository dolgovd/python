# Library sqlite3 is going to be used

import sqlite3

# Create a DB
db = sqlite3.connect('db.sqlite')
cursor = db.cursor()

# Create a table
cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE)
''')

# Insert data
cursor.execute('INSERT INTO users (name, email) VALUES ("John", "john.smith@gmail.com")')
db.commit()

# # Insert multiple records - option 1
cursor.executescript('''
            INSERT INTO users (name, email) VALUES ("Alice", "alice.doe@gmail.com");
            INSERT INTO users (name, email) VALUES ("Nick", "nick.sanders@gmail.com");
''')
db.commit()

# Insert multiple records - option 2
users = [
    ('user1', 'user1@mail.com'),
    ('user2', 'user2@mail.com'),
    ('user3', 'user3@mail.com')
]
cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)
db.commit()

# Fetch data from DB
email = 'john.smith@gmail.com'
cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
res = cursor.fetchone()
print(res)

# Fetch data from DB
cursor.execute('SELECT * FROM users')
res = cursor.fetchall()
print(res)

# Close connection
db.close