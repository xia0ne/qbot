from flask import Flask, request
import requests
from templates import sendmessage

app = Flask(__name__)

administrator = 1223605525

'''
接收消息
'''
@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':
        print(1)
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

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701, reload=True)
