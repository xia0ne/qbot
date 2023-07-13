import threading

from flask import Flask, request
import requests
from templates import sendmessage
from templates import manage
from templates import config
from templates import tools
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

'''
接收消息
'''


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':
        if request.get_json().get('user_id') == config.administrator and request.get_json().get('message')[
                                                                         0:6] == '#admin':
            manage.manage(request.get_json().get('user_id'), request.get_json().get('raw_message'))
        elif request.get_json().get('message')[0:4] == '/bot':
            manage.private(request.get_json().get('user_id'), request.get_json().get('raw_message'))
    elif request.get_json().get('message_type') == 'group':
        if request.get_json().get('message')[0:4] == '/bot':
            manage.group(request.get_json().get('group_id'), request.get_json().get('raw_message'),
                         request.get_json().get('user_id'))

    return 'OK'


'''
@description: 发送私人消息的接口
@method: POST
@param {number: number, msg: msg}
@return: OK/ERROR
'''


@app.route('/api/send/private', methods=["POST"])
def send_private():
    print(request.form)
    try:
        number = request.form.get('number')
        msg = request.form.get('msg')
        resp_dict = {
            'msg_type': 'private',
            'number': number,
            'msg': msg,
        }
        sendmessage.send_msg(resp_dict)
        return 'OK'
    except:
        return 'ERROR'


'''
@description: 发送群消息的接口
@method: POST
@param {number: number, msg: msg}
@return: OK/ERROR
'''


@app.route('/api/send/group', methods=["POST"])
def send_group():
    try:
        number = request.form.get('number')
        msg = request.form.get('msg')
        resp_dict = {
            'msg_type': 'group',
            'number': number,
            'msg': msg,
        }
        sendmessage.send_msg(resp_dict)
        return 'OK'
    except:
        return 'ERROR'


scheduler = BackgroundScheduler()
scheduler.add_job(tools.sendGroup, 'cron', hour='7', minute='35')
scheduler.add_job(tools.snedPrivate, 'cron', hour='7', minute='40')
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)
