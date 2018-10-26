# coding:gbk
from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#设置套接字允许广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#固定接收端的端口号
addr = ('',9999)
sockfd.bind(addr)

while True:
	data,addr = sockfd.recvfrom(2048)
	print('从{}处获得广播消息：{}'.format(addr,data.decode('gbk')))
	
	sockfd.sendto('广播已收到'.encode('gbk'),addr)

sockfd.close()
