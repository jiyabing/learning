from socket import *
from select import *
import sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',9999))
s.listen(10)

#创建IO事件地图
fdmap = {s.fileno():s}

#创建poll对象
p = poll()

#将套接字加入到关注
p.register(s,(POLLIN | POLLERR))

while True:
	#进行监控
	events = p.poll()
	#print(events)
	for fd,event in events:
		if fd == s.fileno():
			connfd,addr = fdmap[fd].accept()
			print('connect from',addr)
			p.register(connfd,POLLIN)
			fdmap[connfd.fileno] = connfd
		elif event & POLLIN:
			data = fdmap[fd].recv(1024)
			if not data:
				p.unregister(fd)
				fdmap[fd].close()
				del fdmap[fd]
			else:
				print(data.decode('gbk'))
				fdmap[fd].send('copyright'.encode('gbk'))
		
