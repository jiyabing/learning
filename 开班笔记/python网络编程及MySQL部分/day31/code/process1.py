#coding:gbk

import multiprocessing as mp
import os
import time

def th1():
    print(os.getppid(),'----',os.getpid())
    print('���緹')
    time.sleep(3)
    print('���緹')
    time.sleep(3)
    print('����')
    time.sleep(2)

def th2():
    print(os.getppid(),'----',os.getpid())
    print('˯��')
    time.sleep(2)
    print('˭���')
    time.sleep(3)

def th3():
    print(os.getppid(),'----',os.getpid())
    print('�򶹶�')
    time.sleep(4)
    print('�򶹶�')
    time.sleep(4)


#���������µĽ��̣��������������¼�
#���ɽ��̶���ֱ��ʾ����������
p1 = mp.Process(target = th1)
p2 = mp.Process(target = th2)
p3 = mp.Process(target = th3)

#ͨ�����ɵĽ��̶��������ӽ���
#�ӽ����и����̵Ĵ���Σ�ֻ����ִֻ�ж�Ӧ�ĺ���
if __name__ =='__main__':
    p1.start()
    p2.start()
    p3.start()

    print('parent PID',os.getpid())

#�����ȴ����ս���
    p1.join()
    p2.join()
    p2.join()

    print('+++++++')
    
    th1()
    th2()
    th3()

