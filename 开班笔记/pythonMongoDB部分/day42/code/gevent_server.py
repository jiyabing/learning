import gevent
import time
from gevent import monkey

#在导入socket前执行，改变ｓｏｃｋｅｔ的阻塞形态
monkey.patch_all()
from socket import *

def server(port):
	s = socket()
	s.bind(('127.0.0.1',port))
	s.listen(5)
	while True:
		c,addr = s.accept()
		print('connect from',addr)
		gevent.spawn(handler,c)

#处理客户端事件
def handler(c):
	while True:
		data = c.recv(1024)
		if not data:
			break
		print('recv:'data.decode())
		c.send(time.ctime().encode())
	c.close()

if __name__ == '__main__':
	server(9999)
