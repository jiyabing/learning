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

things = [th1,th2,th3]
process = []





#ͨ�����ɵĽ��̶��������ӽ���
#�ӽ����и����̵Ĵ���Σ�ֻ����ִֻ�ж�Ӧ�ĺ���
if __name__ =='__main__':
    for th in things:
        p = mp.Process(target=th)
        p.daemon = True
        process.append(p)
        p.start()


    print('===������===')

    #for i in process:
       # i.join()



