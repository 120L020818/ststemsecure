import subprocess
if __name__ == '__main__':
    # res=subprocess.run(['ps','aux'],stdout=subprocess.PIPE)
    # print(res.stdout)
    res=subprocess.run('ps -a | grep main',shell=True,stdout=subprocess.PIPE)
    # res=subprocess.run(['ls','-l'],stdout=subprocess.PIPE)
    mystr=res.stdout.decode('utf-8')
    print(mystr)
    # print(type(mystr))
    # mylist=mystr.split()
    # print(mylist)
    # username=mylist[0]

