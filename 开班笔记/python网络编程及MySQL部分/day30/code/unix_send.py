# coding:gbk


from socket import *
import sys,os


#确定用哪个文件进行通信
server_address = './test'  #当前目录下的test文件

#判断文件存在性，如果已经存在需要处理
if os.path.exists(server_address):
    os.unlink(server_address) #删除已存在的文件

#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM,0)

#绑定本地套接字文件
sockfd.bind(server_address)

#监听
sockfd.listen(5)

#收发消息
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if data:
            print(data.decode('gbk'))
            c.sendall('已收到'.encode('gbk'))
        else:
            break
    c.close()
sockfd.close()