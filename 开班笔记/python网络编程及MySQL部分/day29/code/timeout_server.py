from socket import *
from time import sleep,ctime
import traceback

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(('127.0.0.1',9999))

sockfd.listen(10)

#设置sockfd是超时等待
sockfd.settimeout(5)

while True:
	print('等待连接')
	#捕获BlockingIOError异常并作相应的处理
	try:
		conn,addr = sockfd.accept()
	except Exception:
		traceback.print_exc()
		continue
	print(addr,'已连接')
	
	#recv变为超时等待
	conn.settimeout(5)
	while True:
		data = conn.recv(1024)
		print(data.decode('gbk'))
		if not data:
			print('对方已断开')
			break
		
		conn.send('收到'.encode('gbk'))

	conn.close()

sockfd.close()