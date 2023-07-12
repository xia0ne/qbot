import datetime
import requests


def getTodayContest():
    flag = False
    ans = f"今天是{datetime.date.today().strftime('%Y-%m-%d')}\n"
    url = "https://contests.sdutacm.cn/contests.json"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    contests = response.json()
    for i in contests:
        dt_str = i["start_time"]
        offset_str = dt_str[-6:]
        offset_seconds = int(offset_str[0:3]) * 3600 + int(offset_str[4:6]) * 60
        dt = datetime.datetime.strptime(dt_str[:-6], '%Y-%m-%dT%H:%M:%S')
        utc_dt = dt - datetime.timedelta(seconds=offset_seconds)
        utc8 = utc_dt + datetime.timedelta(hours=8)
        if utc8.date() == datetime.date.today() and i['source'] != 'CSAcademy':
            flag = True
            ans += f"在 {i['source']}上有一场比赛：{i['name']}，开始时间是{utc8.strftime('%Y-%m-%d %H:%M:%S')}\n"
    if not flag:
        ans += "今天没有比赛！休息一下吧！"
    return ans
