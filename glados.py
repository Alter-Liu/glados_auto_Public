import requests
import json
import os

# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # pushplus秘钥 申请地址 http://www.pushplus.plus
    sckeys = os.environ.get("PUSHPLUS_TOKEN", []).split("&")
    # glados账号cookie 直接使用列表，如果需要多个账号则用&分割，这里使用split进行分割
    cookies = os.environ.get("GLADOS_COOKIE", []).split("&")
    # 用户姓名,用于给不同的用户推送不同的信息
    users = os.environ.get("NAMES", []).split("&")
    # 推送内容
    sendContent = ''
    # 所有用户的邮件地址
    emails = []
    # 所有用户剩余天数
    time_users = []
    # 服务器返回消息
    messes = []
    
    if cookies[0] == "":
        print('未获取到COOKIE变量')
        sendContent = '未获取到cookies'
        requests.get(
                'http://www.pushplus.plus/send?token=' + sckeys[0] + '&title=' + "A notice for " + users[0] + '&content=' + sendContent)
        exit(0)
        
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.one'
    }
    
    for cookie in cookies:
        checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                              'user-agent': useragent,
                                              'content-type': 'application/json;charset=UTF-8'},
                                data=json.dumps(payload))
        state = requests.get(url2,
                             headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
        
    # --------------------------------------------------------------------------------------------------------#
       if 'message' in checkin.text and checkin.json()['message'] != '没有权限':
            mess = checkin.json()['message']
            messes.append(mess)
            
            time = state.json()['data']['leftDays']
            time = time.split('.')[0]
            time_users.append(time)
            
            email = state.json()['data']['email']
            emails.append(email)
            print(email + '----结果--' + mess + '----剩余(' + time + ')天')  # 日志输出
            # sendContent += email + '----' + mess + '----剩余 ' + time + ' 天\n'
        else:
            messes.append("cookie已失效")
            emails.append(' ')
            time_users.append(' ') 
        
    # --------------------------------------------------------------------------------------------------------#
    if sckeys != "":
        for sckey, email, time_user, mess, user in zip(sckeys, emails, time_users, messes, users):
            if email == ' ':
                sendContent = '<p>Dear {}</p>'.format(user) + \
                              '<p style="text-indent:2em">{}</p>'.format(mess)
                requests.get(
                    'http://www.pushplus.plus/send?token=' + sckey + '&title=' + "A notice for " + user + '&content=' + sendContent)
            else:
                sendContent = '<p>Dear {}</p>'.format(user) + \
                              '<p style="text-indent:2em">  About your account({}) Check-in feedback information is </p>'.format(email) + '<p style="text-align:center">{}</p>'.format(mess) + \
                              '<p style="text-indent:2em">And the remaining days of your account is</p>'+'<p style="text-align:center"> {} </p>'.format(time_user) + \
                              '<p>Best regards from LawnJerch!</p>'
                requests.get(
                    'http://www.pushplus.plus/send?token=' + sckey + '&title=' + "A notice for " + user + '&content=' + sendContent)
