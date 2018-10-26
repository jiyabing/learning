#coding:gbk
import os,sys
from time import sleep


pid = os.fork()

if pid < 0:
    print('create process failed')

elif pid == 0:
    print('Child process...')
    sleep(2)
    sys.exit(2)

else:
    #设置为非阻塞状态，循环查看子进程状态
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)
        sleep(1)
        print('parent process')
        print(p,status)
        while True:
            pass