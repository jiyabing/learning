import sys
from socket import *
from time import ctime

#从命令行传入ip和端口
if len(sys.argv) < 3:
	print('argv is error!!!')

host = sys.argv[1]
port = int(sys.argv[2])
ADDR = (host,port)
buffersize = 1024

#1.创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#2.绑定ip和端口
print('服务已开启！')
sockfd.bind(ADDR)


#3.收发消息
count = 0
while True:

	#收消息
	data,addr = sockfd.recvfrom(buffersize)
	print(addr,data.decode('gbk'))
	
	count += 1
	
	#发消息
	sockfd.sendto(('[%s]接收到消息' %ctime()).encode('gbk'),addr)
	
	if count > 10:
		print('服务器存储已满，须断开')
		break
	
sockfd.close()