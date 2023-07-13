import sqlite3
from templates import getDB
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE users (qq TEXT)')
# conn.execute('CREATE TABLE groups (id TEXT)')
# conn.execute('CREATE TABLE message (msg TEXT,time TEXT, type TEXT, number TEXT)')
# conn.execute('CREATE TABLE problems (id TEXT,rating TEXT, url TEXT)')
# conn.execute('INSERT INTO problems (id, rating, url) VALUES (?, ?, ?)', ('1', '5', 'http://example.com'))
# conn.execute('CREATE TABLE cfusers (cfname TEXT,realname TEXT)')
# conn.execute('INSERT INTO cfusers (cfname, realname) VALUES (?, ?)', ('Cup_', '菜鸡yrh'))
# conn.commit()
# cursor = conn.execute('SELECT * FROM cfusers WHERE cfname = ?', ('Cup_',))
# users = []
# for row in cursor:
#     users.append(row)
# print(users[0][1])
# conn.close()
# print(getDB.getProblems(1822))

from templates import tools
tools.sendGroup()