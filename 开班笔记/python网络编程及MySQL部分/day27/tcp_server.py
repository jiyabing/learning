# coding:gbk

from socket import *
import sys
import traceback

if len(sys.argv) < 3:
    print('参数输入错误！')
    sys.exit(1)


host = sys.argv[1]
port = sys.argv[2]
addr = (host,int(port))

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind(addr)

sockfd.listen(5)

#设置sockfd是超时等待
sockfd.settimeout(10)

while True:
    #等待客户端连接,将和客户端通信的套接字绑定到connfd
    print('服务器已开启,等待用户连接...')
    try:
        connfd,addr = sockfd.accept()
    except Exception:
        traceback.print_exc()
        print('无客户端连接，本服务即将关闭！')
        break
    print(addr,'已连接')


    while True:
        #收消息
        try:
            data = connfd.recv(1024)
        except ConnectionResetError:
            print(addr,'客户端掉线')
            break
        else:
            if not data:
                print(addr,'已主动断开连接')
                break
        print('收到来自',addr,'的消息：%r' %data.decode('gbk'))

        #发消息
        connfd.send('服务器已收到！'.encode('gbk'))

    #关闭套接字
    connfd.close()

sockfd.close()
print('本服务已关闭！')