from socket import *

host = ''
port = 9999

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)

#设置套接字允许接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#设置端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#固定接收端的端口号
s.bind((host,port))


while True:
	try:
		message,addr = s.recvfrom(4096)
		print('从{}获取的信息是{}'.format(addr,message.decode()))
		
		s.sendto('不是针对谁，在座的各位都是...'.encode(),addr)
	except (KeyboardInterrupt,SyntaxError):
		raise
	except Exception as e:
		print(e)

s.close()