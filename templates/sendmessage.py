'''
发送消息
resp_dict = {
    'msg_type': 'group/private',  # 回复类型（群聊/私聊）
    'number': 123456,  # 回复账号（群号/好友号）
    'msg': 'hello',  # 要回复的消息
}
'''
import socket


def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    client.connect((ip, 5700))
    msg_type = resp_dict['msg_type']
    number = resp_dict['number']
    msg = resp_dict['msg']
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0
