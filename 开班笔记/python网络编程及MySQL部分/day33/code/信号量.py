from multiprocessing import Semaphore,Process,current_process
from time import sleep

#创建信号量初始量3
sem = Semaphore(3)

def fun():
	print('进程 %s 等待信号量'%current_process())
	sem.acquire()
	print('进程 %s 消耗信号量'%current_process())
	sleep(5)
	print('进程 %s 添加信号量'%current_process())
	sem.release()
	
jobs=[]
for i in range(4):
	p = Process(target=fun)
	p.start()
	jobs.append(p)

for i in jobs:
	i.join()
