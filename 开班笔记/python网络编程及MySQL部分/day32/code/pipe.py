from multiprocessing import Process,Pipe
import os,time
#创建一个双向管道
fd1,fd2 = Pipe()

def fun(name):
	time.sleep(1)
	#发送字符串到管道
	fd1.send('hello'+str(name))
	print(os.getppid(),'------',os.getpid())

jobs = []

if __name__ == '__main__':
	for i in range(5):
		p = Process(target = fun,args = (i,))
		jobs.append(p)
		p.start()
	print(os.getpid())

#接受子进程发送的消息
	for i in range(5):
		data = fd2.recv()
		print(data)

	for i in jobs:
		i.join()