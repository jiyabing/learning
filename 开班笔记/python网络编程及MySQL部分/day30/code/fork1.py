#coding:gbk

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('��������ʧ��')
elif pid == 0:
    print('�ӽ��̱�����')

    #�ӽ����Լ���ȡ�Լ���PID
    print('��ȡ�ӽ���pid',os.getpid())

    #�ӽ��̻�ȡ�������̵�PID
    print('��ȡ������pid',os.getppid())
else:
    sleep(1)
    print('���Ǹ�����')

    #������fork����ֵ�����ӽ���PID
    print('pid=',pid)

    #�����̻�ȡ�Լ���PID
    print('��ȡ����pid',os.getpid())