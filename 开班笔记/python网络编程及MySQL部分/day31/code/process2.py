#coding:gbk

from multiprocessing import *
from time import sleep

def worker(sec,msg):
    for i in range(3):
        sleep(sec)
        print('worker msessage:',msg)

#位置传参
#p = Process(target = worker,args = (2,'hello'))

#字典传参
p = Process(name = '子进程1', target = worker,kwargs = {'sec':2,'msg':'hello'})

if __name__ =='__main__':
    p.start()
    
    print('p.name:',p.name)
    print('p.pid:',p.pid)
    print('p.is_alive:',p.is_alive())
    
    p.join()