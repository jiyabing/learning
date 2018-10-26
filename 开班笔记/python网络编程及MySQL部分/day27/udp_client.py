# coding:gbk
from socket import *


#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)

addr = ('127.0.0.1',9999)


while True:
    #发消息
	msg = input('输入发送内容>>')
	if not msg:
	    break
	sockfd.sendto(msg.encode('gbk'),addr)
	
	#收消息
	data,addr = sockfd.recvfrom(1024)
	print(data.decode('gbk'))


sockfd.close()	