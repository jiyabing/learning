# coding:gbk

from socket import *

#�������ݱ��׽���
sockfd = socket(AF_INET,SOCK_DGRAM,0)



#�󶨷�������ַ
addr = ('127.0.0.1',9999)
sockfd.bind(addr)
print('����������')

while True:
    #����Ϣ
	data,addr = sockfd.recvfrom(1024)
	print('�յ�',addr,'��������Ϣ��%r' %data.decode('gbk'))

    #����Ϣ
	sockfd.sendto('���������յ�'.encode('gbk'),addr)

sockfd.close()