#coding:gbk

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')

elif pid == 0:
    #父进程已经退出，打印的将是新的父进程的PID
    sleep(1)
    print('My parent PID：',os.getppid())

else:
    print('Parent PID：',os.getpid())