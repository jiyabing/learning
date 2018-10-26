# coding:gbk

from socket import *
import sys
#文件已经被另一端创建
#需要和另一端使用同一个socket文件
server_address = './test'

try:
    sockfd = socket(AF_UNIX,SOCK_STREAM,0)
    sockfd.connect(server_address)
except error as e:
    print(e)
    sys.exit(1)

#发消息
while True:
    msg = input('输入要发送的内容>>')
    if msg:
        sockfd.sendall(msg.encode('gbk'))
        print(sockfd.recv(1024).decode('gbk'))
    else:
        break 
sockfd.close()