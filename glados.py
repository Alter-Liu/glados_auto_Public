import requests
import json
import os
# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
# pushplus秘钥 申请地址 http://www.pushplus.plus
    sckeys = os.environ.get("PUSHPLUS_TOKEN", []).split("&")
# 推送内容
    sendContent = ''
# glados账号cookie 直接使用列表，如果需要多个账号则用&分割，这里使用split进行分割
    cookies = os.environ.get("GLADOS_COOKIE", []).split("&")
    if cookies[0] == "":
        print('未获取到COOKIE变量') 
        exit(0)
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload={
        'token': 'glados.one'
    }
    for cookie in cookies:
        checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    #--------------------------------------------------------------------------------------------------------#  
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        email = state.json()['data']['email']
        if 'message' in checkin.text:
            mess = checkin.json()['message']
            print(email+'----结果--'+mess+'----剩余('+time+')天')  # 日志输出
            sendContent += email+'----'+mess+'----剩余('+time+')天\n'
        else:
            if sckeys != "":
                for sckey in sckeys:
                    requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email+'cookie已失效')
                    print('cookie已失效')  # 日志输出
     #--------------------------------------------------------------------------------------------------------#   
    if sckeys != "":
        for sckey in sckeys:
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+email+'签到成功'+'&content='+sendContent)


