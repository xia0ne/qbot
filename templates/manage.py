from templates import sendmessage
from templates import getDB
from templates import config
from templates import getTodayContest
from templates import tools


def manage(number, msg):
    msgg = msg.split(' ')
    if msgg[1] == '帮助':
        str = '''
#admin 帮助 查看帮助
#admin 查看当前订阅用户 查看当前订阅用户
#admin 查看数量 查看调用接口次数
        '''
        sendmessage.send_msg({
            'msg_type': 'private',
            'number': number,
            'msg': str,
        })
    elif msgg[1] == '查看当前订阅用户':
        sendmessage.send_msg({
            'msg_type': 'private',
            'number': number,
            'msg': '当前订阅用户：\n' + getDB.getPeople(),
        })
    elif msgg[1] == '查看数量':
        sendmessage.send_msg({
            'msg_type': 'private',
            'number': number,
            'msg': '调用接口次数：\n' + getDB.getLogs(),
        })


def private(number, msg):
    msss = msg.split(' ')
    if msss[1] == 'help':
        str = '''
/bot help 查看帮助
/bot addme 订阅当天的比赛消息
/bot delme 取消订阅当天的比赛消息
/bot status 查看订阅状态
        '''
        sendmessage.send_msg({
            'msg_type': 'private',
            'number': number,
            'msg': str,
        })
    elif msss[1] == 'addme':
        if getDB.findPeople(number):
            sendmessage.send_msg({
                'msg_type': 'private',
                'number': number,
                'msg': "您已经订阅过了,请勿重复订阅",
            })
        else:
            if getDB.addPeople(number):
                sendmessage.send_msg({
                    'msg_type': 'private',
                    'number': number,
                    'msg': "订阅成功\n" + getTodayContest.getTodayContest(),
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'private',
                    'number': number,
                    'msg': "订阅失败，我也不知道为什么",
                })
    elif msss[1] == 'delme':
        if getDB.findPeople(number):
            if getDB.delPeople(number):
                sendmessage.send_msg({
                    'msg_type': 'private',
                    'number': number,
                    'msg': "取消订阅成功，欢迎下次再来",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'private',
                    'number': number,
                    'msg': "取消订阅失败，我也不知道为什么",
                })
        else:
            sendmessage.send_msg({
                'msg_type': 'private',
                'number': number,
                'msg': "您还没有订阅，请先订阅",
            })
    elif msss[1] == 'status':
        if getDB.findPeople(number):
            sendmessage.send_msg({
                'msg_type': 'private',
                'number': number,
                'msg': "您已经订阅了",
            })
        else:
            sendmessage.send_msg({
                'msg_type': 'private',
                'number': number,
                'msg': "您还没有订阅，请先订阅",
            })


def group(number, msg, who):
    msss = msg.split(' ')
    if msss[1] == 'help':
        str = '''
/bot help 查看帮助
/bot contest 查看今日比赛
/bot random xxx 随机一道cfxxx分的题目
/bot cf xxx 查看cf名为xxx是谁
/bot addcf xxx1 xxx2 添加cf名xxx1的名字为xxx2
/bot modcf xxx1 xxx2 修改cf名为xxx1的名字为xxx2
/bot delcf xxx 删除cf名为xxx的名字

'''
        sendmessage.send_msg({
            'msg_type': 'group',
            'number': number,
            'msg': str,
        })
    elif msss[1] == 'contest':
        sendmessage.send_msg({
            'msg_type': 'group',
            'number': number,
            'msg': getTodayContest.getTodayContest(),
        })
    elif msss[1] == 'add':
        if who == config.administrator:
            if getDB.addGroup(number):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "订阅成功",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "订阅失败，我也不知道为什么",
                })
        else:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': "您没有权限",
            })

    elif msss[1] == 'del':
        if who == config.administrator:
            if getDB.delGroup(number):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "取消订阅成功，欢迎下次再来",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "取消订阅失败，我也不知道为什么",
                })
        else:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': "您没有权限",
            })
    elif msss[1] == 'random':
        try:
            if 800 <= int(msss[2]) <= 3500:
                problem = getDB.getProblems(msss[2])
                if problem:
                    msg = f'给您推荐 {problem[1]} 分的题目, 他的链接是 {problem[2]}'
                    sendmessage.send_msg({
                        'msg_type': 'group',
                        'number': number,
                        'msg': msg,
                    })
                else:
                    sendmessage.send_msg({
                        'msg_type': 'group',
                        'number': number,
                        'msg': '没有找到题目',
                    })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': '请输入正确的分数',
                })
        except:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': '请输入正确的分数',
            })
    elif msss[1] == 'cf':
        try:
            if getDB.getcfUsers(msss[2]):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "{} 的cf是 {}".format(msss[2], getDB.getcfUsers(msss[2])),
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': '没有找到用户',
                })
        except:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': '请输入正确的用户名',
            })
    elif msss[1] == 'addcf':
        try:
            # if who == config.administrator:
            if getDB.addcfUsers(msss[2], msss[3]):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "添加成功",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': '添加失败',
                })
        # else:
        #     sendmessage.send_msg({
        #         'msg_type': 'group',
        #         'number': number,
        #         'msg': "您没有权限",
        #     })
        except:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': '请输入正确的用户名',
            })
    elif msss[1] == 'modcf':
        if who == config.administrator:
            if getDB.changecfUsers(msss[2], msss[3]):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "修改成功",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': '修改失败',
                })
        else:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': "您没有权限",
            })
    elif msss[1] == 'delcf':
        if who == config.administrator:
            if getDB.delcfUsers(msss[2]):
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': "删除成功",
                })
            else:
                sendmessage.send_msg({
                    'msg_type': 'group',
                    'number': number,
                    'msg': '删除失败',
                })
        else:
            sendmessage.send_msg({
                'msg_type': 'group',
                'number': number,
                'msg': "您没有权限",
            })
    elif msss[1] == 'allcf':
        # if who == config.administrator:
        sendmessage.send_msg({
            'msg_type': 'group',
            'number': number,
            'msg': getDB.getAllcfUser(),
        })
    else:
        sendmessage.send_msg({
            'msg_type': 'group',
            'number': number,
            'msg': "没有这个指令",
        })
