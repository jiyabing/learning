# coding:gbk
from socket import *


#�������ݱ��׽���
sockfd = socket(AF_INET,SOCK_DGRAM,0)

addr = ('127.0.0.1',9999)


while True:
    #����Ϣ
	msg = input('���뷢������>>')
	if not msg:
	    break
	sockfd.sendto(msg.encode('gbk'),addr)
	
	#����Ϣ
	data,addr = sockfd.recvfrom(1024)
	print(data.decode('gbk'))


sockfd.close()	