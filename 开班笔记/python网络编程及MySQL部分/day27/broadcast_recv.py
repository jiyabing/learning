# coding:gbk
from socket import *

#�������ݱ��׽���
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#�����׽�������㲥
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#�̶����ն˵Ķ˿ں�
addr = ('',9999)
sockfd.bind(addr)

while True:
	data,addr = sockfd.recvfrom(2048)
	print('��{}����ù㲥��Ϣ��{}'.format(addr,data.decode('gbk')))
	
	sockfd.sendto('�㲥���յ�'.encode('gbk'),addr)

sockfd.close()
