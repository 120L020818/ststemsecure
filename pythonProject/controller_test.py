# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import sys

from PyQt5.QtCore import QTimer
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from test import Ui_Form
import subprocess
import json
import csv
import requests

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):

        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.readUserInfo()
        username = self.getUserNameAndShow()
        self.label_placeholder.setText(username)

        self.pushButton.clicked.connect(self.buttonSubmit)
        # self.pushButton.clicked.connect(self.display)

        self.timer = QTimer(self)
        self.count = 0
        self.timer.timeout.connect(self.incProgressBar)
        self.startCount()
    # def display(self):
    #     temp=self.lineEdit.text()
    #     self.label.setText(temp)
    def startCount(self):
        self.timer.start(1000)
    def monitorWrongTime(self):
        pass
    # def visionGame(self):
    #     res = subprocess.run('ps -a | grep main', shell=True, stdout=subprocess.PIPE)
    def gamekill(self,gamename):
        print(f"going to kill {gamename}")
        query = subprocess.run(f'ps -a | grep {gamename}', shell=True, stdout=subprocess.PIPE)
        mystr = query.stdout.decode('utf-8')
        print(mystr)
        if mystr != '':
            innerlist = mystr.split()
            pid = innerlist[0]
            print(pid)
            query2 = subprocess.run(f'kill {pid}', shell=True, stdout=subprocess.PIPE)
            mystr2 = query2.stdout.decode('utf-8')
            print(mystr2)


    def incProgressBar(self):
        playRule={
            '12': 1,
            '18': 2,
        }
        gametime=0
        f=open('user.json','r')
        age=json.load(f)['age']
        if age<12:
            gametime=1
        elif gametime<18:
            gametime=2
        else:
            gametime=3


        value=self.progressBar.value()
        if value+20==100:

            mydata2 = {
                'test': '2333'
            }
            res2=requests.post('http://192.168.0.104:10240/api/knowkill', json=mydata2)

            # res2 = requests.get('http://192.168.0.104:10240/api/knowkill')
            print(res2.url)
            kill2 = res2.json()['gamename']
            print(f'kill:{kill2}')
            self.gamekill(kill2)
            # res =  subprocess.run('ps -a | grep main', shell=True, stdout=subprocess.PIPE)

            self.progressBar.setValue(100)
            mydata = {
                'test': '2333'
            }
            res=requests.post('http://192.168.0.104:10240/api/first', json=mydata)
            print(res.json()['mydata'])

            mylist=res.json()['mydata']
            print(f'mylist:{mylist}')

            f=''
            try:
                f = open('gameInfo.txt', 'r', newline='')
            except:
                f2 = open('gameInfo.txt', 'w', newline='')
                csvwriter = csv.writer(f2)
                for i in mylist:
                    # each row is a json : gamename,gametime,laststart,starttimes,wrongtimes
                    templist = [i['game'],gametime,'0','00:00','0']
                    print(templist)
                    csvwriter.writerow(templist)
                f = open('gameInfo.txt', 'r', newline='')

            csvreader=csv.reader(f)
            datalist=[]
            for row in csvreader:
                print(f"row:{row}")
                datalist.append(row)
            # datalist is a list that stored locally
            print(f'datalist:{datalist}')

            # i want to search
            for i in mylist:
                flag=0
                # i have now
                for j in datalist:
                    # initial  query all data in mylist whether they are in datalist
                    # if not , add them
                    if i['game']==j[0]:
                        print(f"look here!!{i['game']},{j[0]}")
                        flag=1
                        break
                if flag==0:
                    print(f'{i["game"]} was added!')
                    datalist.append( [i['game'],gametime,'0','00:00','0'])

            for i in mylist:
                print('start....')
                query = subprocess.run(f'ps -a | grep {i["game"]}', shell=True, stdout=subprocess.PIPE)
                mystr=query.stdout.decode('utf-8')
                print(mystr)
                flag = 0
                starttime=0
                runningtime=0
                begin=0
                if mystr!='':
                    flag=1
                    innerlist=mystr.split()
                    pid=innerlist[0]
                    query2 = subprocess.run(f'ps -o lstart,etime -p {pid}', shell=True, stdout=subprocess.PIPE)
                    mystr2 = query2.stdout.decode('utf-8')
                    seclist=mystr2.split()
                    print(seclist)
                    starttime=seclist[-2]+'-'+seclist[3]+'-'+seclist[4]+'-'+seclist[5]
                    begin=seclist[-2]
                    runningtime=seclist[-1]

                for j in datalist:
                    # find wangtd game locally and is running
                    if i['game']!=j[0]:
                        continue

                    if  flag==1:
                        onetime=(j[2]==starttime)
                        j[2]=starttime
                        # total time
                        temptar1=runningtime.split(':')
                        temptar2=j[3].split(':')
                        print(temptar1)
                        print(temptar2)
                        totaltime0=int(temptar1[0])+int(temptar2[0])
                        totaltime1=int(temptar1[1])+int(temptar2[1])
                        if totaltime1>=60:
                            totaltime1=totaltime1%60
                            totaltime0=totaltime0+1
                        if onetime==False:
                            j[3]=str(totaltime0)+":"+str(totaltime1)
                            j[4]=str(int(j[4])+1)
                        else:
                            j[3]=runningtime
                        print(j[3])
                        # if 0<=int(begin.split(':')[0]) and  int(begin.split(':')[0])<17:
                        #     j[4]=str(int(j[4])+1)

                    # # can't find wanted game
                    # elif flag==1:
                    #     print(f'game {i["game"]} is running')
                    #     temptar1 = runningtime.split(':')
                    #     temptar2 ='00:00'.split(':')
                    #     totaltime0 = int(temptar1[0]) + int(temptar2[0])
                    #     totaltime1 = int(temptar1[1]) + int(temptar2[1])
                    #     if totaltime1 >= 60:
                    #         totaltime1 = totaltime1 % 60
                    #         totaltime0 = totaltime0 + 1
                    #     mytime = str(totaltime0) + ":" + str(totaltime1)
                    #     test=0
                    #     if 0 <= int(begin.split(':')[0]) and int(begin.split(':')[0]) < 17:
                    #         test = 1
                    #     templist=[i['game'],'2',starttime,mytime,test]
                    #     # print(f'{i["game"]}was added!!!!')
                    #     datalist.append(templist)

            f  =open('gameInfo.txt', 'w', newline='')
            f.truncate(0)

            f2 = open('gameInfo.txt', 'w', newline='')
            csvwriter=csv.writer(f2)
            for i in datalist:
                # each row is a json : gamename,gametime,laststart,starttimes,wrongtimes
                print(i)
                csvwriter.writerow(i)

            print('end....')

            mydict=[]
            mydata2={
                "mydata":datalist
            }
            print(mydata2)
            res = requests.post('http://192.168.0.104:10240/api/update', json=mydata2)
            print(res.json()['mydata'])
            mylist = res.json()['mydata']
            print(f'mylist:{mylist}')
            return

        else:
            self.progressBar.setValue((value+20)%100)
            return



    def getUserNameAndShow(self):
        res = subprocess.run('who', shell=True, stdout=subprocess.PIPE)
        mystr = res.stdout.decode('utf-8')
        mylist = mystr.split()
        print(mylist)
        username = mylist[0]

        mylist = mystr.split()
        mylist.remove(mylist[1])
        mylist.remove(mylist[-1])
        print(mylist)
        f = open('userinfo.txt', 'a', newline='')
        f2 = open('userinfo.txt', 'r', newline='')
        csvreader = csv.reader(f2)
        # if recorded , don't repeat in the file
        for row in csvreader:
            print(f'look here {row}')
            if mylist==row:
                res = requests.post('http://192.168.0.104:10240/api/username', json={'username':username})
                return username

        csvwriter = csv.writer(f)
        csvwriter.writerow(mylist)

        res = requests.post('http://192.168.0.104:10240/api/username', json={'username': username})
        return username


    def readUserInfo(self):
        mydict = ''
        flag = 1
        try:
            f = open('user.json', 'r')
            # if the file exists
            mydict = json.load(f)
            print('you have registered before')

            res = subprocess.run('date +"%Y-%m-%d"', stdout=subprocess.PIPE, shell=True)
            mystr = res.stdout.decode('utf-8')
            mylist = mystr.split('-')
            for i in range(0, 3):
                mylist[i] = int(mylist[i])
            print(mylist)
            mylist2 = [int(mydict['year']), int(mydict['month']), int(mydict['day'])]
            print(mylist2)
            realage = 0
            first = mylist[0] - mylist2[0]
            if first < 0:
                print('time set wrong!!')
            second = 0
            if mylist[1] - mylist2[1] > 0 or ((mylist[1] - mylist2[1]) == 0 and mylist[2] == mylist[2]):
                second = 1
            realage = first + second
            print(realage)
            mydict['age'] = realage
            f = open('user.json', 'w')
            json.dump(mydict, f)
            flag = 1
        except:
            print("you haven't registered before")
            flag = 0

        if flag == 1:
            self.label.setText('you have registered before!!')
            self.pushButton.setDisabled(True)

    def buttonSubmit(self):

        print('buttonSubmit was called')
        myage = self.lineEdit_age.text()
        myear = self.lineEdit_year.text()
        mymon = self.lineEdit_month.text()
        myday = self.lineEdit_day.text()
        mysex = self.checkBox.checkState()
        print(mysex)
        # 0 means girl 2 means boy
        print(type(mysex))
        if mysex == 0:
            mysex = 'girl'
        else:
            mysex = 'boy'
        mydict = {
            'age': myage,
            'year': myear,
            'month': mymon,
            'day': myday,
            'sex': mysex,
        }
        try:
            f = open('user.json', 'r')
            mydict = json.load(f)
        except:
            f = open('user.json', 'w')
            json.dump(mydict, f)


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
