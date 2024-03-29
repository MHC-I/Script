#每天自动签到+10积分，及自动完成每周学习任务
#study_day=5 周几学习
#QNCK=学号;MD5 32位小写加密后的密码;qq号

import requests
import json
import time
import os

def login(username,passwd):
    header={"Host":"home.yngqt.org.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Accept-Language":"zh-CN,zh-Hans;q=0.9","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":"http://home.yngqt.org.cn","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1","Connection":"keep-alive","Referer":"http://home.yngqt.org.cn/qndxx/index.aspx","Content-Length":"78","Cookie":"ASP.NET_SessionId=0lm0czun4pxdfdm0ojujwd3n"}
    data=json.dumps({"txtusername":username,"txtpassword":passwd})
    res=session.post(url=baseurl+"login.ashx",headers=header,data=data)
    print(eval(res.text)["message"])

def qiandao():
    res=session.post(url=baseurl+"user/qiandao.ashx")
    print(eval(res.text)["message"])

def xuexi():
    #第一次进入页面
    res=session.post(url=baseurl+"existsuser.ashx")
    print(eval(res.text)["message"])
    infoid=eval(res.text)["infoid"]
    url=eval(res.text)["url"]
    data=json.dumps({"txtid":infoid})
    #第二次应该是保存学习请求
    res=session.post(url=baseurl+"xuexi.ashx",data=data)
    print(eval(res.text)["message"])

if __name__ == '__main__':
    baseurl = "http://home.yngqt.org.cn/qndxx/"
    #获取环境变量
    study_day=os.environ["study_day"]
    QNCKs = os.environ["QNCK"].split('&')
    for QNCK in QNCKs:
        QNCK=QNCK.split(';')
        username=QNCK[0]
        passwd=QNCK[1]
        qq=QNCK[2]
        #确定session
        session=requests.session()
        #登陆，签到，学习
        login(username,passwd)
        qiandao()
        if time.localtime(time.time())[6]==int(study_day)-1:
            xuexi()