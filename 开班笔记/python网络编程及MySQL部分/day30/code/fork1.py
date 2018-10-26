#coding:gbk

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    print('子进程被创建')

    #子进程自己获取自己的PID
    print('获取子进程pid',os.getpid())

    #子进程获取它父进程的PID
    print('获取父进程pid',os.getppid())
else:
    sleep(1)
    print('这是父进程')

    #父进程fork返回值就是子进程PID
    print('pid=',pid)

    #父进程获取自己的PID
    print('获取进程pid',os.getpid())