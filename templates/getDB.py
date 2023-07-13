import math
import sqlite3

def getSendPeople():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM users ')
    people = []
    for row in cursor:
        people.append(row[0])
    conn.close()
    return people

def getSendGoup():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM groups ')
    groups = []
    for row in cursor:
        groups.append(row[0])
    conn.close()
    return groups

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


def getProblems(a):
    ratings = math.floor(int(a) / 100) * 100
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM problems WHERE rating = ?', (ratings,))
    problems = []
    for row in cursor:
        problems.append(row)
    conn.close()
    import random
    return problems[random.randint(0, len(problems) - 1)]


def getcfUsers(a):
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM cfusers WHERE cfname = ?', (a,))
    users = []
    for row in cursor:
        users.append(row)
    conn.close()
    if len(users) == 0:
        return False
    else:
        return users[0][1]


def addcfUsers(cfname, realname):
    if getcfUsers(cfname):
        return False
    else:
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO cfusers (cfname,realname) VALUES (?,?)', (cfname, realname))
        conn.commit()
        conn.close()
        return True


def changecfUsers(cfname, realname):
    if not getcfUsers(cfname):
        return False
    else:
        conn = sqlite3.connect('database.db')
        conn.execute('UPDATE cfusers SET realname = ? WHERE cfname = ?', (realname, cfname))
        conn.commit()
        conn.close()
        return True


def delcfUsers(cfname):
    if not getcfUsers(cfname):
        return False
    else:
        conn = sqlite3.connect('database.db')
        conn.execute('DELETE FROM cfusers WHERE cfname = ?', (cfname,))
        conn.commit()
        conn.close()
        return True


def getAllcfUser():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM cfusers')
    users = ""
    for row in cursor:
        users += row[0] + " " + row[1] + "\n"
    conn.close()
    return users
