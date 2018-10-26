#coding:gbk

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')

elif pid == 0:
    print('子进程的PID:',os.getpid())

else:
    sleep(1)
    while True:
        pass