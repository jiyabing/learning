#coding:gbk

import os,sys
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')

elif pid == 0:
    print('�ӽ��̵�PID:',os.getpid())
    sleep(2)
    sys.exit(3)

else:
    p,status = os.wait()
    print(p,status)
    print(os.WEXITSTATUS(status))
    while True:
        pass