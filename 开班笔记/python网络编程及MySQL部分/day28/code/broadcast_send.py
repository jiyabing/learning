from socket import *
from time import sleep

#发送广播地址
dest = ('176.215.155.255',9999)

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
	sleep(1)
	s.sendto('你好'.encode(),dest)
	
	data,addr = s.recvfrom(1024)
	print('receive from %s:%s' %(addr,data.decode()))

s.close()