import smtplib
from email.header import Header
from email.mime.text import MIMEText
from random import random

from django.http import JsonResponse, FileResponse, HttpResponse

import csv
import json


def controller_233(request):
    print("已接收到controller_233的请求")
    req = json.loads(request.body)
    print(req)
    return JsonResponse({
        "success": True,
    })


def controller_download1(request):
    f = open('vision', 'rb')
    return FileResponse(f)
def controller_download2(request):
    f = open('user.json', 'rb')
    return FileResponse(f)

def controller_first(request):
    print("已接收到controller_first的请求")
    req = json.loads(request.body)
    print(req)
    mylist = []
    with open("forwardGameInfo.txt", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp = {"game": row[0], "avatime": row[1], "lasttime": row[2], "runningtime": row[3], "wrongtime": row[4]}
            mylist.append(temp)
            print(row)
    return JsonResponse({
        "success": True,
        "mydata": mylist
    })


def controller_second(request):
    print("已接收到controller_second的请求")
    req = json.loads(request.body)
    print(req)
    mylist = []
    with open("backGameInfo.txt", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp = {"game": row[0], "avatime": row[1], "lasttime": row[2], "runningtime": row[3], "wrongtime": row[4]}
            mylist.append(temp)
            # print(row)
    timelist=controller_period()
    # print(f'timelist {timelist}')
    # print(f'mylist {mylist}')

    for i in mylist:
        gamename=i['game']
        for j in timelist:
            if gamename==j[0]:
                print(f'here {i}')
                print(f'here {j}')
                i['period1']=j[1]
                i['period2']=j[2]
                i['period3']=j[3]
                i['period4']=j[4]
    print(f'mylist {mylist}')
    return JsonResponse({
        "success": True,
        "mydata": mylist
    })


def controller_test(request):
    print("已接收到test_controller的请求")
    req = json.loads(request.body)
    print(req)
    wantadd = req['game']
    mylist = []
    with open("forwardGameInfo.txt", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            temp = {"game": row[0], "avatime": row[1], "lasttime": row[2], "runningtime": row[3], "wrongtime": row[4]}
            mylist.append(temp)
            print(row)
    flag = 0
    for i in mylist:
        if wantadd == i['game']:
            print('已经存在该游戏!')
            flag = 1
            break
    if flag == 0:
        temp = {"game": wantadd, "avatime": '0', "lasttime": '0', "runningtime": '00:00', "wrongtime": '0'}
        # temp={"game":wantadd,"isava":"no"}
        mylist.append(temp)
        print(mylist)
        with open("forwardGameInfo.txt", 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            res = []
            for i in mylist:
                temp = [i['game'], i['avatime'], i['lasttime'], i['runningtime'], i['wrongtime']]
                res.append(temp)
            print(res)
            writer.writerows(res)

    return JsonResponse({
        "success": True,
        "mydata": mylist
    })


def controller_delete(request):
    print("已接收到controller_delete的请求")
    req = json.loads(request.body)
    print(req)
    wantdel = req['game']
    mylist = []
    with open("forwardGameInfo.txt", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp = {"game": row[0], "avatime": row[1], "lasttime": row[2], "runningtime": row[3], "wrongtime": row[4]}
            # temp = {"game": row[0], "isava": row[1]}
            mylist.append(temp)
            print(row)
    for i in range(0, len(mylist)):
        print(mylist[i])
        print(wantdel)
        if wantdel == mylist[i]['game']:
            mylist.remove(mylist[i])
            break
    with open("forwardGameInfo.txt", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        res = []
        for i in mylist:
            temp = [i['game'], i['avatime'], i['lasttime'], i['runningtime'], i['wrongtime']]
            res.append(temp)
        print(res)
        writer.writerows(res)

    return JsonResponse({
        "success": True,
        "mydata": mylist
    })


def controller_update(request):
    print("已接收到controller_update的请求")
    req = json.loads(request.body)
    print(req)
    mylist = req['mydata']
    with open("backGameInfo.txt", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        res = []
        for i in mylist:
            temp = [i[0], i[1], i[2], i[3], i[4]]
            res.append(temp)
        print(res)
        writer.writerows(res)
    temp = 233
    return JsonResponse({
        "success": True,
        "mydata": 233
    })



def controller_email(request):
    print("已接收到controller_email的请求")

    req = json.loads(request.body)

    print(req)

    from_addr = '565852435@qq.com'
    password = 'gplblhngalnybfhe'

    print(req)
    username = req['username']

    smtp_server = 'smtp.qq.com'

    msg = MIMEText(f'您的孩子:{username}已超量使用今日限额!', 'plain', 'utf-8')
    msg['From'] = Header('天际PC管理系统')
    msg['To'] = Header('用户')
    msg['Subject'] = Header('天际PC管理系统告警邮件')

    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)

    server.login(from_addr, password)
    to_addr = '835766751@qq.com'
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()

    return JsonResponse({
        "success": True,
    })

def controller_username(request):
    print("已接收到controller_username的请求")
    req = json.loads(request.body)
    username=req['username']
    f=open('username.txt','w')
    f.write(username)
    return JsonResponse({
        "success": True,
    })

def controller_getusername(request):
    print("已接收到controller_getusername的请求")
    f=open('username.txt','r')
    username =f.read()
    print(username)
    return JsonResponse({
        "success": True,
        "username":username
    })
def controller_kill(request):
    print("已接收到controller_kill的请求")
    req = json.loads(request.body)
    gamename = req['gamename']
    f=open('kill.txt','w')
    f.write(gamename)
    return JsonResponse({
        "success": True,
    })
def controller_knowkill(request):
    print("已接收到controller_knowkill的请求")
    # req = json.loads(request.body)
    f=open('kill.txt','r')
    gamename=f.read()
    print(type(gamename))
    f2=open('kill.txt','w')
    f2.truncate(0)
    return JsonResponse({
        "success": True,
        "gamename": gamename,
    })

def controller_period():
    print("已接收到controller_period的请求")
    f=open('backGameInfo.txt','r')
    f1=open('eachPeriod.txt','r')
    gamelist = []
    csvreader1 = csv.reader(f1)
    for i in csvreader1:
        # print(i)
        gamelist.append(i)
    # print(gamelist)

    # 一天分为四个时间段,分别记录0-6点,6-12点,12-18点,18-24点四个段的游戏开启时间
    csvreader=csv.reader(f)
    # csvwriter=csv.writer(f2)
    for i in csvreader:
        name=i[0]
        time=i[2]
        timelist=time.split('-')
        print(timelist)
        print(name)
        startTime=timelist[-1]
        startHour=startTime.split(':')
        startHour=int(startHour[0])



    return gamelist



