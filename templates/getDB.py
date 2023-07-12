import sqlite3


def getPeople():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM users')
    people = []
    for row in cursor:
        people.append(row[0])
    conn.close()
    return str(len(people))


def ToLogs(msg, time, type, number):
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO message (msg,time,type,number) VALUES (?,?,?,?)', (msg, time, type, number))
    conn.commit()
    conn.close()


def getLogs():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM message')
    logs = []
    for row in cursor:
        logs.append(row)
    conn.close()
    return str(len(logs))


def addPeople(number):
    if findPeople(number):
        return False
    else:
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO users (qq) VALUES (?)', (number,))
        conn.commit()
        conn.close()
        return True


def delPeople(number):
    if findPeople(number):
        conn = sqlite3.connect('database.db')
        conn.execute('DELETE FROM users WHERE qq = ?', (number,))
        conn.commit()
        conn.close()
        return True
    else:
        return False


def findPeople(number):
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM users WHERE qq = ?', (number,))
    if len(cursor.fetchall()) == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True


def findGroup(number):
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM groups WHERE id = ?', (number,))
    if len(cursor.fetchall()) == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True

def addGroup(number):
    if findGroup(number):
        return False
    else:
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO groups (id) VALUES (?)', (number,))
        conn.commit()
        conn.close()
        return True

def delGroup(number):
    if findGroup(number):
        conn = sqlite3.connect('database.db')
        conn.execute('DELETE FROM groups WHERE id = ?', (number,))
        conn.commit()
        conn.close()
        return True
    else:
        return False