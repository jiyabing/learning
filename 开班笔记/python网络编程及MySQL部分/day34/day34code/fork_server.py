from socket import *
import os,sys
import signal

#封装客户端函数
def client_handler(c):
	try:
		print('子进程接受客户端的请求',c.getpeername())
		while True:
			data = c.recv(1024).decode()
			if not data:
				break
			print(data)
			c.send('服务器以收到'.encode())
	except (KeyboardInterrupt,SystemExit):
		raise
	except Exception as e:
		print(e)
	c.close()
	#结束子进程
	sys.exit(0)
	

#创建套接字
host = ''#等同于'127.0.0.1'
port = 9999

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)

print('父进程%d等待客户端连接'%os.getpid())
while True:
	try:
		c,addr = s.accept()
	except KeyboardInterrupt:
		raise
	except Exception as e:
		print(e)
		continue
	#为新的客户端创建进程
	
	#处理僵尸进程
	signal.signal(signal.SIGCHLD,signal.SIG_IGN)
	
	pid = os.fork()
	if pid < 0:
		print('创建子进程失败')
		c.close()
		continue
	elif pid == 0:
		s.close()
		#处理客户端请求
		client_handler(c)
	else:
		c.close()
		continue
