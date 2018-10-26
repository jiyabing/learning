#coding:gbk

import multiprocessing as mp
import os
import time

def th1():
    print(os.getppid(),'----',os.getpid())
    print('吃早饭')
    time.sleep(3)
    print('吃午饭')
    time.sleep(3)
    print('吃晚饭')
    time.sleep(2)

def th2():
    print(os.getppid(),'----',os.getpid())
    print('睡觉')
    time.sleep(2)
    print('谁午觉')
    time.sleep(3)

def th3():
    print(os.getppid(),'----',os.getpid())
    print('打豆豆')
    time.sleep(4)
    print('打豆豆')
    time.sleep(4)

things = [th1,th2,th3]
process = []





#通过生成的进程对象启动子进程
#子进程有父进程的代码段，只不过只执行对应的函数
if __name__ =='__main__':
    for th in things:
        p = mp.Process(target=th)
        p.daemon = True
        process.append(p)
        p.start()


    print('===父进程===')

    #for i in process:
       # i.join()



