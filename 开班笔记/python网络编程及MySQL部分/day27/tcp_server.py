# coding:gbk

from socket import *
import sys
import traceback

if len(sys.argv) < 3:
    print('�����������')
    sys.exit(1)


host = sys.argv[1]
port = sys.argv[2]
addr = (host,int(port))

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(addr)

sockfd.listen(5)

#����sockfd�ǳ�ʱ�ȴ�
sockfd.settimeout(10)

while True:
    #�ȴ��ͻ�������,���Ϳͻ���ͨ�ŵ��׽��ְ󶨵�connfd
    print('�������ѿ���,�ȴ��û�����...')
    try:
        connfd,addr = sockfd.accept()
    except Exception:
        traceback.print_exc()
        print('�޿ͻ������ӣ������񼴽��رգ�')
        break
    print(addr,'������')


    while True:
        #����Ϣ
        try:
            data = connfd.recv(1024)
        except ConnectionResetError:
            print(addr,'�ͻ��˵���')
            break
        else:
            if not data:
                print(addr,'�������Ͽ�����')
                break
        print('�յ�����',addr,'����Ϣ��%r' %data.decode('gbk'))

        #����Ϣ
        connfd.send('���������յ���'.encode('gbk'))

    #�ر��׽���
    connfd.close()

sockfd.close()
print('�������ѹرգ�')