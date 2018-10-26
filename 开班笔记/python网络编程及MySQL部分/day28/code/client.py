from socket import *
sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(('176.215.155.131',9999))
print('连接成功')

for i in range(5):
    sockfd.send('hello world'.encode('gbk'))


data = sockfd.recv(1024)
print(data.decode('gbk'))



sockfd.close()