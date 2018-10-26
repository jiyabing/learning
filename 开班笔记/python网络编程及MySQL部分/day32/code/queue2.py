from multiprocessing import Process,Queue
import time

#创建消息队列
q = Queue()

def fun1():
	time.sleep(1)
	q.put('进程1')

def fun2():
	time.sleep(2)
	print('取消息：',q.get())

p1 = Process(target = fun1)
p2 = Process(target = fun2)
if __name__ == "__main__":	

	p1.start()
	p2.start()

	p1.join()
	p2.join()