from socket import *

#1.创建流式套接字
sockfd = socket(AF_INET,SOCK_STREAM,0)

#2.绑定ip和端口
sockfd.bind(('127.0.0.1',9999))

#3.设置监听套接字，创建监听队列
sockfd.listen(5)


#4.等待客户端连接
print('wait for connect...')
connfd,addr = sockfd.accept()
print('connect from',addr)

#5.收发消息
#接收数据
data = connfd.recv(1024)
print(data)

#发送数据
connfd.send('来，确认下眼神'.encode())

#6.关闭套接字
connfd.close()
sockfd.close()
