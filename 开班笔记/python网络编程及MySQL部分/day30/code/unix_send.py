# coding:gbk


from socket import *
import sys,os


#ȷ�����ĸ��ļ�����ͨ��
server_address = './test'  #��ǰĿ¼�µ�test�ļ�

#�ж��ļ������ԣ�����Ѿ�������Ҫ����
if os.path.exists(server_address):
    os.unlink(server_address) #ɾ���Ѵ��ڵ��ļ�

#���������׽���
sockfd = socket(AF_UNIX,SOCK_STREAM,0)

#�󶨱����׽����ļ�
sockfd.bind(server_address)

#����
sockfd.listen(5)

#�շ���Ϣ
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if data:
            print(data.decode('gbk'))
            c.sendall('���յ�'.encode('gbk'))
        else:
            break
    c.close()
sockfd.close()