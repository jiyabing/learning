# coding:gbk

from socket import *
import sys
#�ļ��Ѿ�����һ�˴���
#��Ҫ����һ��ʹ��ͬһ��socket�ļ�
server_address = './test'

try:
    sockfd = socket(AF_UNIX,SOCK_STREAM,0)
    sockfd.connect(server_address)
except error as e:
    print(e)
    sys.exit(1)

#����Ϣ
while True:
    msg = input('����Ҫ���͵�����>>')
    if msg:
        sockfd.sendall(msg.encode('gbk'))
        print(sockfd.recv(1024).decode('gbk'))
    else:
        break 
sockfd.close()