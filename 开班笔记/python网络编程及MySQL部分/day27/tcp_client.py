# coding:gbk

from socket import *
import sys
from time import sleep

if len(sys.argv) < 3:
    print('参数输入错误!')
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]
addr = (host,int(port))

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM,0)


#连接服务端
while True:
    try:
        sockfd.connect(addr)
    except ConnectionRefusedError:
        print('服务器未开启,请稍后再连接!')
        sleep(5)
        continue
    else:
        print('连接成功！')
        break


while True:
    #发消息
    msg = input('输入内如>>')
    if not msg:
        break
    sockfd.send(msg.encode('gbk'))


    #收消息
    data = sockfd.recv(1024)
    print(data.decode('gbk'))

#关闭套接字
sockfd.close()
