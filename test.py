import sqlite3
conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE users (qq TEXT)')
conn.execute('INSERT INTO users (qq) VALUES ("123456")')
conn.commit()
cursor = conn.execute('SELECT qq FROM users')
for row in cursor:
    print(row[0])
conn.close()