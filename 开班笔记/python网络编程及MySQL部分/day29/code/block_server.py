from socket import *
from time import sleep,ctime

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(('127.0.0.1',9999))

sockfd.listen(10)

#设置sockfd是非阻塞状态
sockfd.setblocking(False)

while True:
	print('等待连接')
	#捕获BlockingIOError异常并作相应的处理
	try:
		conn,addr = sockfd.accept()
	except BlockingIOError:
		sleep(2)
		print(ctime())
		continue
	print(addr,'已连接')
	
	#recv变为非阻塞
	#conn.setblocking(False)
	while True:
		data = conn.recv(1024)
		print(data.decode('gbk'))
		if not data:
			print('对方已断开')
			break
		
		conn.send('copyright'.encode('gbk'))

	conn.close()

sockfd.close()