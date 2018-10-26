import socket
from threading import *
import os, sys

host = '127.0.0.1'
port = 9999

#处理具体的客户端请求
def handler(connfd):
	print('Got connection from',connfd.getpeername())
	while True:
		data = connfd.recv(1024).decode()
		if not data:
			break
		connfd.send(b'receive your message')
	connfd.close()

#创建套接字
s = socket.socket()
s.bind((host,port))
#设置端口可重用
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.listen(5)

#主线程循环接受客户端连接
while True:
	try:
		c,addr = s.accept()
	except KeyboardInterrupt:
		raise
	except Exception as e:
		print(e)
		continue
	
	t = Thread(target=handler,args=(c,))
	#主线程结束，子线程也退出
	t.setDaemon(True)
	t.start()
s.close()
