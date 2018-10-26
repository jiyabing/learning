#coding:gbk

from socket import *
from time import sleep


#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#将套接字设置为允许接收广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#设置广播端ip地址和端口
addr = ('176.215.155.255',9999)



while True:
	#发送广播消息
	sockfd.sendto('请注意，以下播报一则重要消息'.encode('gbk'),addr)
	sleep(2)
	
	data,addr = sockfd.recvfrom(1024)
	print('收到',addr,'发来的消息：%s' %data.decode('gbk'))

sockfd.close()
