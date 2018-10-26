# coding:gbk

from socket import *
import sys
from time import sleep

if len(sys.argv) < 3:
    print('�����������!')
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]
addr = (host,int(port))

#�����׽���
sockfd = socket(AF_INET,SOCK_STREAM,0)


#���ӷ����
while True:
    try:
        sockfd.connect(addr)
    except ConnectionRefusedError:
        print('������δ����,���Ժ�������!')
        sleep(5)
        continue
    else:
        print('���ӳɹ���')
        break


while True:
    #����Ϣ
    msg = input('��������>>')
    if not msg:
        break
    sockfd.send(msg.encode('gbk'))


    #����Ϣ
    data = sockfd.recv(1024)
    print(data.decode('gbk'))

#�ر��׽���
sockfd.close()
