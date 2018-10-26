# coding:gbk

from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)



#绑定服务器地址
addr = ('127.0.0.1',9999)
sockfd.bind(addr)
print('服务已启动')

while True:
    #收消息
	data,addr = sockfd.recvfrom(1024)
	print('收到',addr,'发来的消息：%r' %data.decode('gbk'))

    #发消息
	sockfd.sendto('服务器已收到'.encode('gbk'),addr)

sockfd.close()