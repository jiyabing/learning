#coding:gbk

from socket import *
from time import sleep


#�������ݱ��׽���
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#���׽�������Ϊ������չ㲥
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#���ù㲥��ip��ַ�Ͷ˿�
addr = ('176.215.155.255',9999)



while True:
	#���͹㲥��Ϣ
	sockfd.sendto('��ע�⣬���²���һ����Ҫ��Ϣ'.encode('gbk'),addr)
	sleep(2)
	
	data,addr = sockfd.recvfrom(1024)
	print('�յ�',addr,'��������Ϣ��%s' %data.decode('gbk'))

sockfd.close()
