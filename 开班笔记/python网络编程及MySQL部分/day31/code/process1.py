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


#创建三个新的进程，关联上面三个事件
#生成进程对象分别表示这三个进程
p1 = mp.Process(target = th1)
p2 = mp.Process(target = th2)
p3 = mp.Process(target = th3)

#通过生成的进程对象启动子进程
#子进程有父进程的代码段，只不过只执行对应的函数
if __name__ =='__main__':
    p1.start()
    p2.start()
    p3.start()

    print('parent PID',os.getpid())

#阻塞等待回收进程
    p1.join()
    p2.join()
    p2.join()

    print('+++++++')
    
    th1()
    th2()
    th3()

