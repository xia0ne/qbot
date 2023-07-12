import sqlite3
from templates import getDB
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE users (qq TEXT)')
# conn.execute('CREATE TABLE groups (id TEXT)')
# conn.execute('CREATE TABLE message (msg TEXT,time TEXT, type TEXT, number TEXT)')
# conn.execute('CREATE TABLE problems (id TEXT,rating TEXT, url TEXT)')
# conn.execute('INSERT INTO problems (id, rating, url) VALUES (?, ?, ?)', ('1', '5', 'http://example.com'))
# conn.commit()
# conn.close()
print(getDB.getProblems(1822))