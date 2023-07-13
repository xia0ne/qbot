import random
import time

from templates import getDB
from templates import sendmessage
from templates import getTodayContest


def getRandFace():
    return '[CQ:face,id=' + str(random.randint(0, 170)) + ']'


def snedPrivate():
    peoples = getDB.getSendPeople()
    for people in peoples:
        sendmessage.send_msg({
            'msg_type': 'private',
            'number': people,
            'msg': getTodayContest.getTodayContest()
        })
        time.sleep(1)


def sendGroup():
    groups = getDB.getSendGoup()
    for group in groups:
        sendmessage.send_msg({
            'msg_type': 'group',
            'number': group,
            'msg': getTodayContest.getTodayContest()
        })
        time.sleep(1)
